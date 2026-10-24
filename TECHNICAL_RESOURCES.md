# Additional Power Foundation Model Resources

Candidate open-source resources for the PowerFM catalogue, using a concise project-entry format. This file is submitted separately so maintainers can decide whether and how to incorporate any entries into the README.

## GridSFM: Foundation Model for AC Optimal Power Flow

#### [Explore GridSFM: Open Model, Code, and Power-Grid Data](https://github.com/microsoft/GridSFM)

**GridSFM** is an open foundation model for approximating AC optimal power flow across different power-grid topologies. It represents the grid as a heterogeneous graph and predicts operating states such as bus voltages, generator dispatch, and branch flows, supporting scenario screening and warm-starting conventional AC-OPF solvers.

![GridSFM architecture](https://www.microsoft.com/en-us/research/wp-content/uploads/2026/05/image-2.jpg)

- **Code and data pipeline:** [GitHub](https://github.com/microsoft/GridSFM)
- **Released checkpoints and datasets:** [Hugging Face collection](https://huggingface.co/collections/microsoft/gridsfm)
- **Paper:** [GridSFM: A Foundation Model for AC Optimal Power Flow](https://www.microsoft.com/en-us/research/publication/gridsfm-a-foundation-model-for-ac-optimal-power-flow/)

## PriceFM: Foundation Model for Probabilistic Electricity-Price Forecasting

#### [Explore PriceFM: Model, Dataset, and Fine-Tuning Tutorial](https://github.com/runyao-yu/PriceFM)

**PriceFM** is a foundation model for probabilistic day-ahead electricity-price forecasting across connected European market regions. It combines a Mixture-of-Experts feature projection with a sparse graph mask informed by transmission topology to generate quantile forecasts across regions and lead times.

![PriceFM architecture](https://raw.githubusercontent.com/runyao-yu/PriceFM/main/Figure/PriceFM_structure.PNG)

- **Pretrained model:** [Hugging Face](https://huggingface.co/RunyaoYu/PriceFM)
- **Dataset:** [Hugging Face Datasets](https://huggingface.co/datasets/RunyaoYu/PriceFM)
- **Paper:** [arXiv:2508.04875](https://arxiv.org/abs/2508.04875)

## Supporting Datasets and Benchmarks

These resources support power-domain model training or evaluation but are not themselves pretrained foundation models.

- **[PowerGridQA](https://github.com/Hannaancode/PowerGridQA)** — A power-system question-answer dataset covering dynamics, operations, reliability, and reasoning. The repository reports 28,852 question-answer pairs. [Research paper](https://ieeexplore.ieee.org/abstract/document/11345118).
- **[PowerCodeBench](https://github.com/huiwxing/PowerCodeBench)** — An execution-validated benchmark for LLM-generated power-system analysis code using executable `pandapower` programs and reference results. The repository describes 2,000 tasks. [Research paper](https://doi.org/10.1016/j.aei.2026.105328).

Check code, model, and dataset licensing independently before reuse; terms may differ between project components.

---

This is a documentation-only candidate resource list. It does not change implementation code or dependencies. The existing `README.md` is intentionally left unchanged for maintainers to handle.
