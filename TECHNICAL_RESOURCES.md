# Additional Technical Resources for Power Foundation Models

This note records candidate open-source resources that complement the projects already listed in the PowerFM README. It is intentionally separate from `README.md` and contains no implementation changes.

## 1. PriceFM — Probabilistic Electricity-Price Forecasting Foundation Model

- **Resource type:** Pretrained foundation model, multi-region dataset, fine-tuning tutorial, and research paper.
- **Problem addressed:** Day-ahead electricity prices are interdependent across connected market regions and uncertain over time. PriceFM is designed to forecast multiple regions and forecast horizons jointly, while producing quantile forecasts rather than only a single point estimate.
- **Dataset:** The paper and project documentation describe a European dataset spanning **24 countries and 38 regions**, from 2022 to 2026. The March 2026 project update reports a change from hourly to **15-minute (quarter-hourly)** resolution. Inputs include historical electricity prices and exogenous features such as load, solar, and wind forecasts.
- **Architecture:** Regional price and exogenous features are mapped into a shared representation using a **Mixture-of-Experts (MoE) projection**. The model then applies a **sparse graph mask derived from transmission topology** to represent cross-region relationships. Hierarchical quantile heads produce probabilistic forecasts for multiple regions and lead times. This is the central technical distinction from a generic time-series model that treats regions independently or has no explicit grid-topology prior.
- **Evaluation protocol:** The project’s March 2026 update reports evaluation expanded from one test fold in 2024–2025 to three test folds in 2025–2026, with both full-shot and cross-region zero-shot evaluation. These settings are useful when assessing transfer to regions with limited or no task-specific training data. Consult the paper and repository for exact metrics and baseline configurations rather than inferring performance from the project summary.
- **Architecture figure:**  
  ![PriceFM model architecture](https://raw.githubusercontent.com/runyao-yu/PriceFM/main/static/images/PriceFM_structure.PNG)  
  *Figure: PriceFM’s feature-fusion/MoE projection, topology-informed graph block, and hierarchical quantile forecasting heads. Source: official project repository.*
- **Artifacts and references:** [Official code repository](https://github.com/runyao-yu/PriceFM) · [Pretrained model](https://huggingface.co/RunyaoYu/PriceFM) · [Dataset](https://huggingface.co/datasets/RunyaoYu/PriceFM) · [Paper](https://arxiv.org/abs/2508.04875) · [Project page and forecast examples](https://runyao-yu.github.io/PriceFM/)
- **Licensing:** The Hugging Face model and dataset pages display **CC BY 4.0**. This should not be assumed to cover the GitHub source code or every artifact; check the repository’s current license and each artifact’s terms separately before reuse.
- **Why it is relevant to PowerFM:** PriceFM is a direct power-domain foundation-model example with a public model artifact, dataset, and paper. Its topology-aware, probabilistic forecasting setup makes it relevant to electricity markets, renewable integration, and cross-region forecasting.

## 2. PowerGridQA — Power-System Reasoning Dataset

- **Resource type:** Domain-specific question–answer dataset for LLM training and evaluation; not a pretrained foundation model.
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

These resources are categorized separately because a pretrained model, a training dataset, and an evaluation benchmark are different technical artifacts. PriceFM is the direct foundation-model entry; PowerGridQA and PowerCodeBench are included as supporting resources for domain reasoning and executable evaluation. Model/data versions and licenses can change, so consult the linked upstream sources before reuse. This file does not change `README.md`, add software dependencies, or introduce implementation code.
