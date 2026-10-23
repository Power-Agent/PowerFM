# Additional Technical Resources for Power Foundation Models

This note records candidate open-source resources that complement the projects already listed in the PowerFM README. It is intentionally separate from `README.md` and contains no implementation changes.

## 1. GridSFM — Foundation Model for AC Optimal Power Flow

- **Resource type:** Open-source power-system foundation model, inference code, pretrained checkpoint, and grid/operating-scenario data pipeline.
- **Released artifacts:** The official GitHub repository provides model inference code, example scenarios, a data pipeline, and a test suite. The open GridSFM-Open checkpoint and associated grid datasets are linked through the official Hugging Face collection.
- **Problem addressed:** AC optimal power flow (AC-OPF) seeks a low-cost generator dispatch while satisfying nonlinear electrical and operational constraints. Conventional solvers can be computationally expensive when repeated across many operating scenarios.
- **Architecture:** GridSFM represents the network as a graph containing bus, generator, and branch features. A block-structured discrete neural operator processes these graph features through topology-aware attention blocks. Output heads predict an AC operating point—including voltage states, generator dispatch and branch flows—and a feasibility/stress classification. Physics-based penalties complement solver-generated supervision.
- **Training and evaluation scale:** Microsoft Research’s release article reports training across more than 150 base grid topologies and roughly half a million scenarios. On its 54-grid test mix, the article reports a 2.23% median generation-cost gap for GridSFM-Open and a 1.66× geometric-mean AC-OPF solver speedup when using model predictions as warm starts. These are project-reported results, not independent validation; see the source for test-set and metric details.
- **Scope caveat:** The open GridSFM-Open release targets research-scale grids up to 4,000 buses. Microsoft describes GridSFM-Premier as a production-scale tier, but its blog states that the larger tier is not included in the open release. Do not imply that Premier checkpoints are publicly downloadable.
- **Architecture figure:**  
  ![GridSFM model architecture](https://www.microsoft.com/en-us/research/wp-content/uploads/2026/05/image-2.jpg)  
  *Figure: GridSFM embeds bus, generator, and branch features, processes them through topology-aware attention blocks, and predicts an AC operating point plus a feasibility score. Source: Microsoft Research.*
- **Project references:** [Official code and data pipeline](https://github.com/microsoft/GridSFM) · [Model and dataset collection](https://huggingface.co/collections/microsoft/gridsfm) · [Microsoft Research publication](https://www.microsoft.com/en-us/research/publication/gridsfm-a-foundation-model-for-ac-optimal-power-flow/) · [Microsoft Research technical overview and reported results](https://www.microsoft.com/en-us/research/blog/gridsfm-a-new-small-foundation-model-for-the-electric-grid/)
- **License:** The official repository states that its top-level MIT license covers the model package. Check the repository and individual data/model artifacts for any component-specific terms before reuse.
- **Why it is relevant to PowerFM:** GridSFM is a directly relevant, recent, open power-grid foundation model for topology-generalizing AC-OPF inference, scenario screening, and solver warm-starting. It is distinct from the broader GridFM community entry already present in the PowerFM README.

## 2. PriceFM — Probabilistic Electricity-Price Forecasting Foundation Model

- **Resource type:** Pretrained foundation model, multi-region dataset, fine-tuning tutorial, and research paper.
- **Problem addressed:** Day-ahead electricity prices are interdependent across connected market regions and uncertain over time. PriceFM is designed to forecast multiple regions and forecast horizons jointly, while producing quantile forecasts rather than only a single point estimate.
- **Dataset:** The paper and project documentation describe a European dataset spanning **24 countries and 38 regions**, from 2022 to 2026. The March 2026 project update reports a change from hourly to **15-minute (quarter-hourly)** resolution. Inputs include historical electricity prices and exogenous features such as load, solar, and wind forecasts.
- **Architecture:** Regional price and exogenous features are mapped into a shared representation using a **Mixture-of-Experts (MoE) projection**. The model then applies a **sparse graph mask derived from transmission topology** to represent cross-region relationships. Hierarchical quantile heads produce probabilistic forecasts for multiple regions and lead times. This is the central technical distinction from a generic time-series model that treats regions independently or has no explicit grid-topology prior.
- **Evaluation protocol:** The project’s March 2026 update reports evaluation expanded from one test fold in 2024–2025 to three test folds in 2025–2026, with both full-shot and cross-region zero-shot evaluation. These settings are useful when assessing transfer to regions with limited or no task-specific training data. Consult the paper and repository for exact metrics and baseline configurations rather than inferring performance from the project summary.
- **Architecture figure:**  
  ![PriceFM model architecture](https://raw.githubusercontent.com/runyao-yu/PriceFM/main/Figure/PriceFM_structure.PNG)  
  *Figure: PriceFM’s feature-fusion/MoE projection, topology-informed graph block, and hierarchical quantile forecasting heads. Source: official project repository.*
- **Artifacts and references:** [Official code repository](https://github.com/runyao-yu/PriceFM) · [Pretrained model](https://huggingface.co/RunyaoYu/PriceFM) · [Dataset](https://huggingface.co/datasets/RunyaoYu/PriceFM) · [Paper](https://arxiv.org/abs/2508.04875) · [Project page and forecast examples](https://runyao-yu.github.io/PriceFM/)
- **Licensing:** The Hugging Face model and dataset pages display **CC BY 4.0**. This should not be assumed to cover the GitHub source code or every artifact; check the repository’s current license and each artifact’s terms separately before reuse.
- **Why it is relevant to PowerFM:** PriceFM is a direct power-domain foundation-model example with a public model artifact, dataset, and paper. Its topology-aware, probabilistic forecasting setup makes it relevant to electricity markets, renewable integration, and cross-region forecasting.

## 3. PowerGridQA — Power-System Reasoning Dataset

- **Resource type:** Domain-specific question–answer dataset for LLM training and evaluation; not a pretrained foundation model.
- **Technical focus:** Power-system dynamics, grid operations, and reliability, using textbook-derived questions, operational lessons, and reasoning-oriented scenarios.
- **Reported scale:** The repository README reports 23,368 textbook questions, 4,696 operational-insight questions, and 788 reasoning scenarios (28,852 pairs total).
- **Why it is relevant:** It provides domain-specific reasoning data for evaluating or adapting language models beyond general-purpose benchmarks.
- **Links:** [Official repository](https://github.com/Hannaancode/PowerGridQA) · [IEEE Xplore paper](https://ieeexplore.ieee.org/abstract/document/11345118)
- **Licensing note:** A clear dataset reuse license was not confirmed in this review. Check the repository's current license and source-data terms before reuse.

## 4. PowerCodeBench — Execution-Validated Power-System Code Benchmark

- **Resource type:** Benchmark dataset and reproducible evaluation artifacts; not a pretrained foundation model.
- **Technical focus:** Evaluates LLM-generated power-system analysis code using executable `pandapower` programs and reference results, rather than judging answers only as text.
- **Reported scale:** The repository describes 2,000 frozen tasks and provides a verification script and evidence artifacts for reported results.
- **Why it is relevant:** It offers a concrete way to assess whether language models can produce working power-system analysis programs, complementing model and dataset catalogues.
- **Links:** [Official repository](https://github.com/huiwxing/PowerCodeBench) · [Research paper](https://doi.org/10.1016/j.aei.2026.105328)
- **License:** The repository distinguishes CC BY 4.0 for benchmark data/documentation from Apache 2.0 for source code. Follow the repository's license notes for individual components.

## Scope and verification notes

These resources are categorized separately because foundation models, training datasets, and evaluation benchmarks are different technical artifacts. GridSFM and PriceFM are direct foundation-model entries; PowerGridQA and PowerCodeBench are supporting resources for domain reasoning and executable evaluation. Model/data versions and licenses can change, so consult the linked upstream sources before reuse. This file intentionally does not change `README.md`, add software dependencies, or introduce implementation code.
