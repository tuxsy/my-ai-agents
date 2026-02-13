# Data Analysis Agent

An agent that performs statistical analysis on numerical datasets and provides insights.

## Features
- Load and manage multiple datasets
- Calculate statistical measures (mean, median, mode, standard deviation, etc.)
- Compare datasets
- Detect outliers
- Identify trends

## Usage

```python
from agents.data_analysis.data_agent import DataAnalysisAgent

# Create an agent
agent = DataAnalysisAgent(name="Analyst")

# Load data
sales = [100, 150, 120, 180, 200]
agent.load_data("sales", sales)

# Analyze
analysis = agent.analyze("sales")
print(analysis)

# Find trends
trends = agent.find_trends("sales")
print(trends)

# Detect outliers
outliers = agent.detect_outliers("sales", threshold=2.0)
print(outliers)
```

## Running the Example

```bash
python agents/data_analysis/data_agent.py
```

## Example Output

```
[DataAnalyst] Loaded dataset 'sales' with 10 data points
[DataAnalyst] Summary:
Total datasets: 3

Dataset: sales
  - Data points: 10
  - Mean: 193.00
  - Range: [100, 280]

Sales Analysis:
{
  "dataset": "sales",
  "count": 10,
  "mean": 193.0,
  "median": 195.0,
  "min": 100,
  "max": 280,
  "range": 180
}
```
