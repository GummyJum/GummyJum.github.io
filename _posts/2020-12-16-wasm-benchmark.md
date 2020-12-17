---
layout: post
title:  "Wasm-Go Benchmark"
date:   2020-12-16 20:00:51 +0200
categories: Technical
tags: [Golang, Wasm]
---

I dived into [Wasm](https://webassembly.org/) on the weekend since I was intrigued by the potential for running distributed applications at scale with nothing but a web-browser.

I tried to convert parts of the Go benchmark at [The Benchmarks Game](https://benchmarksgame-team.pages.debian.net/benchmarksgame/index.html) to Wasm and test the overhead.

The results were conclusive the overhead was significant and reached an order of magnitude for some of the programs so I don't think I will be using it for scientific computing any time soon.

Still, Wasm was surprisingly efficient and comparable to the native implementation for few programs.

There are many applications that can benefit from using Wasm.
I have a feeling that this won't be my last Wasm project.

[The code along with detailed results can be accessed via GitHub](https://github.com/GummyJum/wasm_benchmark).
