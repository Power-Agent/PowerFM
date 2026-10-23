# PowerFM
PowerFM is an open-source repository for foundation models in the power and energy domain. It both maintains original projects and collects community-contributed open-source projects, featuring fine-tuned and domain-trained models for tasks like load forecasting, fault detection, grid simulation, and agent control.


## 🚀 Getting Started with PowerFM


### OpenPowerBench: Transformer-based Foundation Models

#### [Explore the Dataset and Benchmark for Power System Foundation Models Across Multiple Scales and Topologies](https://github.com/OpenPowerBench/OpenPowerBench)

**OpenPowerBench** is a first-of-its-kind open-source, multi-task, cross-temporal dataset designed to support training and evaluation of foundation models in power systems. OpenPowerBench includes both topology-dependent tasks (e.g., power flow, optimal power flow, contingency analysis) and topology-independent tasks (e.g., load forecasting, price prediction), supported by a modular data generation pipeline for scalable benchmarking across synthetic and real-world scenarios.

![Data Structure](data_structure.png)

![Data Generation Pipeline](data_generation_pipeline.png)


### GridLDM: Language-Conditioned Latent Diffusion Models

#### [Explore GridLDM for Cross-Domain Power-System Time-Series Synthesis](https://github.com/cyuting940612/GridLDM)

**GridLDM** is a unified latent diffusion framework for controllable power-system time-series generation across heterogeneous domains, including EV charging, commercial load, wind generation, solar generation, and transient voltage response. GridLDM learns a shared latent generative prior and uses natural-language prompts with cross-attention to condition synthetic time-series generation across different data lengths, temporal structures, and operating contexts.

[![GridLDM framework](GridLDM.png)](https://github.com/cyuting940612/GridLDM)


### GridFM: Graph Neural Network (GNN)-based Foundation Models

#### [Explore the Dataset and Graph for GridFM](https://github.com/gridfm)

**GridFM Community** The GridFM project pioneers the concept of FMs for the electric power grid to be trained on grid data – as opposed to text data – with the overarching goal to develop the underlying technology to cope with the increasing complexity and uncertainties of a faster growing grid (e.g., due to hyperscalar data centers, crypto mining etc.). More information about GridFM Community can be found [here](https://gridfm.org/)


### GridSFM: Foundation Model for AC Optimal Power Flow

#### [Explore GridSFM: Open Model, Code, and Power-Grid Data](https://github.com/microsoft/GridSFM)

**GridSFM** is an open foundation model for approximating AC optimal power flow across different power-grid topologies. It represents the grid as a heterogeneous graph and predicts operating states such as bus voltages, generator dispatch, and branch flows. The model is designed to support fast scenario screening and warm-starting conventional AC-OPF solvers.

![GridSFM architecture](https://www.microsoft.com/en-us/research/wp-content/uploads/2026/05/image-2.jpg)

- **Code and data pipeline:** [GitHub](https://github.com/microsoft/GridSFM)
- **Released checkpoints and datasets:** [Hugging Face collection](https://huggingface.co/collections/microsoft/gridsfm)
- **Paper:** [GridSFM: A Foundation Model for AC Optimal Power Flow](https://www.microsoft.com/en-us/research/publication/gridsfm-a-foundation-model-for-ac-optimal-power-flow/)


### PriceFM: Foundation Model for Probabilistic Electricity-Price Forecasting

#### [Explore PriceFM: Model, Dataset, and Fine-Tuning Tutorial](https://github.com/runyao-yu/PriceFM)

**PriceFM** is a foundation model for probabilistic day-ahead electricity-price forecasting across connected European market regions. It combines a Mixture-of-Experts feature projection with a sparse graph mask informed by transmission topology to generate quantile forecasts across regions and lead times.

![PriceFM architecture](https://raw.githubusercontent.com/runyao-yu/PriceFM/main/Figure/PriceFM_structure.PNG)

- **Pretrained model:** [Hugging Face](https://huggingface.co/RunyaoYu/PriceFM)
- **Dataset:** [Hugging Face Datasets](https://huggingface.co/datasets/RunyaoYu/PriceFM)
- **Paper:** [arXiv:2508.04875](https://arxiv.org/abs/2508.04875)


### Supporting Datasets and Benchmarks

The following open resources support power-domain model training and evaluation.

- **[PowerGridQA](https://github.com/Hannaancode/PowerGridQA)** — A power-system question-answer dataset covering dynamics, operations, reliability, and reasoning. The repository reports 28,852 question-answer pairs. [Research paper](https://ieeexplore.ieee.org/abstract/document/11345118).
- **[PowerCodeBench](https://github.com/huiwxing/PowerCodeBench)** — An execution-validated benchmark for LLM-generated power-system analysis code, using executable `pandapower` programs and reference results. The repository describes 2,000 tasks. [Research paper](https://doi.org/10.1016/j.aei.2026.105328).

Check the code, model, and dataset licenses independently before reusing project resources; licensing may differ between components.


### mAIEnergy: Multimodal Foundation Models for Energy

#### [Explore the mAIEnergy Dataset and Workflow](https://zenodo.org/records/16401633)

**mAIEnergy** is a unified, open-access multimodal corpus designed to support Continual Pre-Training (CPT) of Large Language Models (LLMs) and the development of Retrieval-Augmented Generation (RAG) systems in the energy domain. The dataset integrates heterogeneous energy-related information into structured, machine-readable formats, enabling seamless integration into modern AI and multimodal learning pipelines.

The corpus is organized into four top-level modules—textual, numerical, geospatial, and imagery—each accompanied by structured metadata and reproducible processing workflows. In total, the dataset contains approximately 50,000 textual documents, 20,000 images, 25 million numerical time-series records, and 2 million geospatial and relational data entries, primarily focusing on the European energy system.

![mAIEnergy Dataset Overview](mAIEnergy.webp)

Detailed datasets and fine-tuned models can be found below:
- **Dataset**: [Zenodo Repository](https://zenodo.org/records/16401633)
- **Trained/Fine-tuned Models**: [Hugging Face Model Hub](https://huggingface.co/ubitech-edg/models)

### RAG-based Foundation Models

#### [Explore the Datacenter Siting Assistant: Solvtra](https://huggingface.co/spaces/zhangqianleo/datacenterAgent)

**Datacenter Siting Assistant: Solvtra** is a tool leverages RAG by incorporating datacenter-specific data, including local regulations, environmental reports, and infrastructure details. As a result, it can provide detailed information for potential datacenter locations, such as land and electricity prices, and generate a map illustrating existing datacenter sites and relevant infrastructure.



## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guidelines](https://power-agent.github.io/) for details.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

### Core Team
[Shaohuai Liu](https://liushaohuai5.github.io/), [Yuting Cai](https://www.linkedin.com/in/yuting-cai/), [Alban Puech](https://www.alban-puech.fr/), 
[Costas Mylonas](https://www.linkedin.com/in/costas-mylonas-a0ab761b6/),
[Magda Foti](https://www.linkedin.com/in/magda-foti/),
[Qian Zhang](https://www.linkedin.com/in/qian-zhang-75323111b/) 

### Special Thanks
- All contributors who help make this project better
- [The Power and AI Initiative (PAI) at Harvard SEAS](https://pai.seas.harvard.edu/)
