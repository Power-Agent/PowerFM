# Additional Technical Resources for Power Foundation Models

This note records candidate open-source resources that complement the projects already listed in the PowerFM README. It is intentionally separate from `README.md` and contains no implementation changes.

## 1. PriceFM — Probabilistic Electricity-Price Forecasting

- **Resource type:** Pretrained forecasting model, dataset, fine-tuning tutorial.
- **Technical focus:** Probabilistic day-ahead electricity-price forecasting. The project describes a graph-informed model and a mixture-of-experts architecture for market-aware forecasting.
- **Data and model availability:** The official repository links a Hugging Face dataset and provides pretrained weights and a fine-tuning notebook. Its README reports that the data was extended through 2026 with quarter-hourly resolution.
- **Why it is relevant:** It covers electricity-market price uncertainty, a task not explicitly represented by the currently listed grid-operation and time-series generation projects.
- **Links:** [Official repository](https://github.com/runyao-yu/PriceFM) · [Dataset](https://huggingface.co/datasets/RunyaoYu/PriceFM) · [Paper](https://arxiv.org/abs/2508.04875)
- **Licensing note:** A root-level LICENSE file was not confirmed during this review. Verify the licenses for code, dataset, and model weights separately before describing them as openly licensed.

## 2. PowerGridQA — Power-System Reasoning Dataset

- **Resource type:** Domain-specific question–answer dataset for LLM training and evaluation.
- **Technical focus:** Power-system dynamics, grid operations, and reliability, using textbook-derived questions, operational lessons, and reasoning-oriented scenarios.
- **Reported scale:** The repository README reports 23,368 textbook questions, 4,696 operational-insight questions, and 788 reasoning scenarios (28,852 pairs total).
- **Why it is relevant:** It provides domain-specific reasoning data for evaluating or adapting language models beyond general-purpose benchmarks.
- **Links:** [Official repository](https://github.com/Hannaancode/PowerGridQA) · [IEEE Xplore paper](https://ieeexplore.ieee.org/abstract/document/11345118)
- **Licensing note:** A clear dataset reuse license was not confirmed in this review. Check the repository's current license and source-data terms before reuse.

## 3. PowerCodeBench — Execution-Validated Power-System Code Benchmark

- **Resource type:** Benchmark dataset and reproducible evaluation artifacts; not a pretrained foundation model.
- **Technical focus:** Evaluates LLM-generated power-system analysis code using executable `pandapower` programs and reference results, rather than judging answers only as text.
- **Reported scale:** The repository describes 2,000 frozen tasks and provides a verification script and evidence artifacts for reported results.
- **Why it is relevant:** It offers a concrete way to assess whether language models can produce working power-system analysis programs, complementing model and dataset catalogues.
- **Links:** [Official repository](https://github.com/huiwxing/PowerCodeBench) · [Research paper](https://doi.org/10.1016/j.aei.2026.105328)
- **License:** The repository distinguishes CC BY 4.0 for benchmark data/documentation from Apache 2.0 for source code. Follow the repository's license notes for individual components.

## Scope and verification notes

These resources are categorized separately because a pretrained model, a training dataset, and an evaluation benchmark are different technical artifacts. Project capabilities and dataset counts above are based on the linked project documentation and should be rechecked against the upstream repositories before reuse. This file does not claim that every resource is a foundation model, and it does not establish licensing beyond what the projects explicitly document.
