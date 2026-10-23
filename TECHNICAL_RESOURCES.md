# Additional Power Foundation Model Resources

This contribution follows the project-entry style used in the PowerFM README while keeping the existing README unchanged, as requested. The entries below focus on recent, open-source power-domain foundation models; related datasets and benchmarks are listed separately.

## GridSFM: Foundation Model for AC Optimal Power Flow

#### [Explore GridSFM: Open Model, Code, and Power-Grid Data](https://github.com/microsoft/GridSFM)

**GridSFM** is an open foundation model for approximating AC optimal power flow (AC-OPF) across different power-grid topologies. It represents the grid as a heterogeneous graph and uses a block-structured discrete neural operator with topology-aware attention and diffusion. The model predicts bus voltage states, generator dispatch, branch flows, and a feasibility score, supporting fast scenario screening and warm-starting conventional AC-OPF solvers.

The official release describes training across 150+ base grid topologies and roughly half a million scenarios. On its reported 54-grid test mix, GridSFM-Open achieved a 2.23% median generation-cost gap and a 1.66× geometric-mean solver speedup when used as a warm start. These are upstream-reported results, not an independent replication. The open checkpoint is intended for research-scale grids up to 4,000 buses; the larger Premier tier is not part of the open release.

![GridSFM architecture](https://www.microsoft.com/en-us/research/wp-content/uploads/2026/05/image-2.jpg)

*GridSFM architecture. Source: [Microsoft Research](https://www.microsoft.com/en-us/research/blog/gridsfm-a-new-small-foundation-model-for-the-electric-grid/).*

- **Code and data pipeline:** [GitHub](https://github.com/microsoft/GridSFM)
- **Released checkpoints and datasets:** [Hugging Face collection](https://huggingface.co/collections/microsoft/gridsfm)
- **Paper:** [GridSFM: A Foundation Model for AC Optimal Power Flow](https://www.microsoft.com/en-us/research/publication/gridsfm-a-foundation-model-for-ac-optimal-power-flow/)

## PriceFM: Foundation Model for Probabilistic Electricity-Price Forecasting

#### [Explore PriceFM: Model, Dataset, and Fine-Tuning Tutorial](https://github.com/runyao-yu/PriceFM)

**PriceFM** is a foundation model for probabilistic day-ahead electricity-price forecasting across connected European market regions. Its architecture combines a Mixture-of-Experts feature projection with a sparse graph mask informed by transmission topology, then generates hierarchical quantile forecasts across regions and lead times. This makes it relevant to price uncertainty, cross-region transfer, and renewable-related market forecasting.

The project reports data spanning 24 countries and 38 regions, with quarter-hourly resolution in its 2026 update. The repository provides pretrained weights and a fine-tuning notebook.

![PriceFM architecture](https://raw.githubusercontent.com/runyao-yu/PriceFM/main/Figure/PriceFM_structure.PNG)

*PriceFM model architecture. Source: [official repository](https://github.com/runyao-yu/PriceFM).*

- **Pretrained model:** [Hugging Face](https://huggingface.co/RunyaoYu/PriceFM)
- **Dataset:** [Hugging Face Datasets](https://huggingface.co/datasets/RunyaoYu/PriceFM)
- **Paper:** [arXiv:2508.04875](https://arxiv.org/abs/2508.04875)

**Licensing note:** Check code, model, and dataset licenses independently before reuse; a license shown for one artifact should not be assumed to cover every project component.

## Related Supporting Resources

The following projects support power-domain model training or evaluation but are **not themselves pretrained foundation models**.

- **[PowerGridQA](https://github.com/Hannaancode/PowerGridQA)** — A power-system question–answer dataset covering dynamics, operations, reliability, and reasoning scenarios. The repository reports 28,852 question–answer pairs. [Research paper](https://ieeexplore.ieee.org/abstract/document/11345118). Verify dataset reuse permissions and source-data terms before reuse.
- **[PowerCodeBench](https://github.com/huiwxing/PowerCodeBench)** — An execution-validated benchmark for LLM-generated power-system analysis code, using executable `pandapower` programs and reference results. The repository describes 2,000 tasks and distinguishes licenses for benchmark materials and source code. [Research paper](https://doi.org/10.1016/j.aei.2026.105328).

## Scope

These entries are intended as additional candidate resources for the PowerFM catalogue. Model results and license terms are summarized from the linked upstream sources and should be checked there before reuse. This is a documentation-only contribution: it does not modify `README.md`, add dependencies, or change implementation code.
