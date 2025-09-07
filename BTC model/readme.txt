# README.md

# Modular Endogenous BTC Price Model

## Overview
This project implements a **modular endogenous model for Bitcoin (BTC) price dynamics**. The model is designed with **parallel pipeline stages** (A, B, C, D) that all funnel into a master pipeline, producing estimated BTC price where average bitcoin miner is profitable, having bands where it is to be expected that every miner is profitable and only best miners are profitable. Based on historical and data.

The modular, parallel design allows each stage to be developed, tested, and maintained independently while integrating seamlessly into the master workflow.


## Pipeline Structure


- **Stage A**: Data Ingestion and Cleaning
  - Every pipeline contains Dataloader class which is custom made to work with corresponding dataset
  - Cleans and formats data for further use

- **Stage B**: Data processing
  - Every pipeline contains Pipeline class which is custom made to transform corresponding raw data into usable form
  - Prepares input variables for the model.

- **Stage C**: Endogenous Model Computation
  - Every pipeline module ends with pipeline function that initialises data loading and pipeline processing data for further use
  - Output of this is input for master pipeline

- **Stage D**: processing and visualization
  - Master pipeline imports all dependencies from pipelines and processes the data
  - After data is turned into estimated price it gets visualized

- **Master Pipeline**: Combines all parallel stages conceptually to produce model


## Key Features
- Modular design emphasising independent stage development and parallel integration.
- Demonstrates workflow structuring and logical problem decomposition.
- Illustrates pipeline thinking applicable to data analysis and modelling.
- Highlights planning and organisation skills in complex Python projects.


## Usage (Conceptual)
- The project demonstrates the design and structure of a modular, parallel pipeline.
- It can be used as a conceptual reference for building similar Python pipelines.
- Focus is on the workflow, stage interactions, and logical organisation, rather than executable code.

- estimated price is where average miner is expected to breaks even
- overbought price is where every miners are expected to break even
- oversold price is where best miners are expected to break even


## Skills Demonstrated
- Python programming concepts
- Modular and parallel workflow design
- Logical structuring of complex processes
- Problem-solving and analytical thinking
- Conceptual data processing and modeling


