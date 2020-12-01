# Rogue Cloud with Nomad
!["one cloud to rule them all and in the darkness bind them"](one_cloud_to_rule_them_all.png)

*"one cloud to rule them all and in the darkness bind them"*

## preface
Nomad is an orchestration tool for deploying and managing applications. It has no dependencies and require almost no configuration making it the perfect tool for a rogue cloud for your underground projects.
If you are a low tier engineer/researcher in an High-Tech company and find yourself in a shortage of computing power this is the post for you. 

Putting your hands on shiny hardware can be a difficult task and sometimes you don't want all the attention that is involved in the process. But what about the company's old servers that on a busy day have CPU utilization rate of one percent? what about your colleagues workstations? Using Nomad you can revive those servers, conquer those workstations and untap the realms of high performance computing on foreign hardware.

Since using Linux for distributed computing has widespread documentation but many office environments are Windows based, this tutorial is mainly focused on Windows.

## Requirements

1. Nomad single binary.
2. Rusty servers / workstations with remote access means. 
3. Understanding that you are responsible for your own actions and the ideas presented here are for educational purpose only.

![](i_am_a_man_of_simple_things.jpeg)

## Configuring and Deploying Nomad

Nomad has two type of agents, server and a client. Where clients run tasks and the server is responsible for managing the cluster (both can be used as the cluster endpoint). 

The following config files are for a single server setup and was tested for over 20 nodes. For better resilience one can use multiple nodes setup.

```
# server.conf
data_dir  = "C:/nomad"
server {
  enabled          = true
  bootstrap_expect = 1
}
plugin "raw_exec" {
  config {
    enabled = true
  }
}
```

```
# client.conf
data_dir  = "C:/nomad"
client {
  enabled       = true
  server_join {
   retry_join = [ "1.1.1.1" ]
  }
}
plugin "raw_exec" {
  config {
    enabled = true
  }
}
```

Gather your list of hosts to hosts.txt

```
hostname1
hostname2
...
```

Assuming you have the same credentials to all of those hosts (Admin Password)

You can now share the nomad single Go binary and config files using the network. (I put them in a single directory and share using the windows 10 network sharing option, right click on folder > Properties > Sharing > Share > Share, thus it is now available to every host on the LAN via \\myhost\nomadir)

After that initialize the nomad server on your workstation from the command line

```
nomad agent -config server.conf
```

And after a few seconds of waiting you can visit the beautiful Nomad UI on http://localhost:4646/ui.

We are now ready to deploy Nomad to all the other hosts, using PAExec

```
paexec @hosts.txt -u Admin -p Password -d \\myhost\nomadir\nomad agent -config \\myhost\nomadir\client.conf
```

Or alternatively using SSH (for example via Ansible which has widespread documentation).

You can now wait and watch the army of nodes that are connecting to your Nomad cluster in the UI clients tab.

## Raw-Exec for the Nomad Ninja
To run docker image on remote workstation it is required that the remote station would have a docker driver, but although docker is common, I found it not common enough. 

Assume that you have your binaries (or even your source) in a compact package you can run them via one of Nomads distinct features, the Raw-Exec driver.

The beauty of this is its simplicity, you can run virtually (as a figure of speech) on any environment without prior configuration as long as your project requirements are met (like in the good old days of the wild west of binaries).

Thus for zero exposure one can upload his binaries to the storage of his choice and run a workstation based stealth high performance computing cluster.

Nomad features like artifact stanza, resources stanza, and env stanza are extremely useful in those covert jobs and work smoothly (which is a big deal for a multi-platform native orchestrator).

![](spartan.jpg)

*The Nomad Spartan*

## Sidenote: Why Nomad is excelent for Map-Reduce
Nomad versatile arsenal is also perfect for a Map-Reduce pipeline.

A pipeline that perform an element wise operation on a Dataset followed by a summery operation is called a Map-Reduce pipeline. It is simple generic data-heavy pipeline template that I found repeating in many projects.

Map-Reduce pipelines are common for data-science since generating an insight out a the haystack often requires some initial processing on the hay.

Training a machine learning model is many times a Map-Reduce pipeline since you have a set of elements that you want to download, sort, filter and finally dump to your model endpoint.

The Map operation can be done via Parametric job configuration and the reduce via service job that waits for all the Map operations to complete successfully and then performs the Reduce operation. 

One can concatenate pipelines and create fairly intricate machine for no cost and with high visibility.

## Conclusion

Nomad is the perfect tool for the simple engineer to abuse any stranded compute power with zero configuration and maximum profit.

It is simple but extensive and easy enough to manage even when you don't have a DevOps team to back you up.

My motivation for writing this sales pitch for Nomad is that my initial experience with Nomad that was harsh for its lack in documentation and examples at the time (which got a lot better since then). After the initial frustration I felt like it is the single best cloud platform that is currently out there for the rebel engineer.
