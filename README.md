# CharpMet - Eurocode 3 Steel Construction Calculator

## Overview

CharpMet is an educational application for Eurocode 3 (EN 1993-1-1) implementation in the context of steel construction design. It provides computational tools to assist students in the "Charpente Métallique" (Steel Construction) course at HELMo Gramme.

## Purpose

This project implements key design criteria and calculations from Eurocode 3, enabling students to:
- Classify steel sections according to EN 1993-1-1
- Calculate section resistance (flexion, compression, shear)
- Analyze stability of compressed members (buckling)
- Evaluate flexural resistance of beams

## Project Structure

### Main Modules

- **Chap_4.py** - Section Classification
  - Classification of cross-sections
  - Corner behavior analysis
  - Tube classification
  
- **Chap_5.py** - Section Resistance
  - Bending resistance (flexion)
  - Compression resistance
  - Shear resistance
  - Combined effects (M, N, V interactions)
  
- **Chap_6.py** - Stability of Members
  - Buckling analysis
  - Critical stress calculations
  
- **Chap_7.py** - Flexural Member Design
  - Lateral-torsional buckling
  - Critical moment calculations

### Supporting Files

- **constant.py** - Material properties and design factors
  - Young's modulus (E = 210000 MPa)
  - Poisson's ratio (ν = 0.3)
  - Reduction factors for different steel grades
  - Safety factors (γ_M)

## Installation

### Setup Instructions

1. **Download the project** - Obtain the complete CharpMet project folder
2. **Create a working folder** - Choose a location on your computer where you want to store the program (e.g., `C:\Users\YourName\Documents\CharpMet` or `~/Downloads/CharpMet`)
3. **Copy all files** - Dump/extract the entire project into your chosen folder, ensuring the structure is preserved:
   - All `.py` files at the root level (Chap_4.py, Chap_5.py, etc.)
   - All subfolders (Func_Chap4/, Func_Chap5/, Func_Chap6/, Func_Chap7/)
4. **Verify installation** - You should have all modules and supporting files in place

### Requirements

- Python 3.x
- No additional external libraries required (uses Python standard library only)

### Tested On

This project has been successfully tested on:
- **Graph 35+ II** (MicroPython v1.9.4)
- **Graph 90** (MicroPython v1.9.4)

## How to Use

This application is designed to work alongside the **formulaire (formula sheet)** provided in the course. 

### Units

All inputs and outputs use the following units:
- **Forces**: N (Newtons)
- **Dimensions**: mm (millimeters)
- **Moments**: N·mm (Newton-millimeters)

Please ensure your input values are converted to these units before running the calculations.

### Key Principle

**Use the end functions directly** - You do not need to call intermediate functions. The program will automatically ask for and calculate all necessary intermediate values. 

#### Example Workflow: M+M+V Interaction Check

For **M+N+V interaction** analysis, follow this sequence:
1. Run **Chap_4.py** to classify the section
2. Run **Chap_5.py** and select the **Int_M_M_N** function
3. Follow the script prompts - the program will automatically:
   - Request input parameters
   - Calculate the reduced plastic moment
   - Compute interaction checks
   - Return the final result

Simply follow the on-screen instructions and refer to the formulaire as needed.

### Running the Application

Run the main scripts to access interactive menus:

```bash
python Chap_4.py  # Section classification tools
python Chap_5.py  # Section resistance calculations
python Chap_6.py  # Member stability analysis
python Chap_7.py  # Flexural member design
```

Follow the on-screen prompts and refer to the formulaire for design parameters and reference values.

<!-- ## Standards Reference

This application implements the design procedures from:
- **EN 1993-1-1:2005** - Eurocode 3: Design of steel structures - Part 1-1: General rules and rules for buildings -->

## Course Information

- **Course**: Charpente Métallique (Steel Construction)
- **Institution**: HELMo Gramme
- **Level**: Master 1
