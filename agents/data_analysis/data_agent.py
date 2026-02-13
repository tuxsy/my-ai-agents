"""
Data Analysis Agent
An agent that analyzes datasets and provides insights.
"""

from typing import List, Dict, Any, Optional
import statistics


class DataAnalysisAgent:
    """Agent for analyzing numerical datasets."""
    
    def __init__(self, name="DataAnalyst"):
        self.name = name
        self.datasets: Dict[str, List[float]] = {}
    
    def load_data(self, name: str, data: List[float]):
        """Load a dataset for analysis."""
        self.datasets[name] = data
        print(f"[{self.name}] Loaded dataset '{name}' with {len(data)} data points")
    
    def analyze(self, dataset_name: str) -> Dict[str, Any]:
        """Perform comprehensive analysis on a dataset."""
        if dataset_name not in self.datasets:
            return {"error": f"Dataset '{dataset_name}' not found"}
        
        data = self.datasets[dataset_name]
        
        if not data:
            return {"error": "Dataset is empty"}
        
        analysis = {
            "dataset": dataset_name,
            "count": len(data),
            "sum": sum(data),
            "mean": statistics.mean(data),
            "median": statistics.median(data),
            "min": min(data),
            "max": max(data),
            "range": max(data) - min(data),
        }
        
        # Add standard deviation and variance if more than one data point
        if len(data) > 1:
            analysis["stdev"] = statistics.stdev(data)
            analysis["variance"] = statistics.variance(data)
        
        # Add mode if available
        try:
            analysis["mode"] = statistics.mode(data)
        except statistics.StatisticsError:
            analysis["mode"] = None
        
        return analysis
    
    def compare(self, dataset1: str, dataset2: str) -> Dict[str, Any]:
        """Compare two datasets."""
        if dataset1 not in self.datasets or dataset2 not in self.datasets:
            return {"error": "One or both datasets not found"}
        
        data1 = self.datasets[dataset1]
        data2 = self.datasets[dataset2]
        
        comparison = {
            "dataset1": dataset1,
            "dataset2": dataset2,
            "mean_diff": statistics.mean(data1) - statistics.mean(data2),
            "median_diff": statistics.median(data1) - statistics.median(data2),
            "size_diff": len(data1) - len(data2),
        }
        
        return comparison
    
    def detect_outliers(self, dataset_name: str, threshold: float = 2.0) -> List[float]:
        """Detect outliers using standard deviation method."""
        if dataset_name not in self.datasets:
            return []
        
        data = self.datasets[dataset_name]
        
        if len(data) < 2:
            return []
        
        mean = statistics.mean(data)
        stdev = statistics.stdev(data)
        
        outliers = [x for x in data if abs(x - mean) > threshold * stdev]
        
        return outliers
    
    def get_summary(self) -> str:
        """Get a text summary of all datasets."""
        if not self.datasets:
            return "No datasets loaded."
        
        summary = f"[{self.name}] Summary:\n"
        summary += f"Total datasets: {len(self.datasets)}\n\n"
        
        for name, data in self.datasets.items():
            summary += f"Dataset: {name}\n"
            summary += f"  - Data points: {len(data)}\n"
            if data:
                summary += f"  - Mean: {statistics.mean(data):.2f}\n"
                summary += f"  - Range: [{min(data)}, {max(data)}]\n"
            summary += "\n"
        
        return summary
    
    def find_trends(self, dataset_name: str) -> Dict[str, Any]:
        """Identify basic trends in the data."""
        if dataset_name not in self.datasets:
            return {"error": f"Dataset '{dataset_name}' not found"}
        
        data = self.datasets[dataset_name]
        
        if len(data) < 2:
            return {"trend": "insufficient data"}
        
        # Simple trend detection
        increasing = sum(1 for i in range(1, len(data)) if data[i] > data[i-1])
        decreasing = sum(1 for i in range(1, len(data)) if data[i] < data[i-1])
        
        total_changes = increasing + decreasing
        
        if total_changes == 0:
            trend = "constant"
        elif increasing > decreasing * 1.5:
            trend = "increasing"
        elif decreasing > increasing * 1.5:
            trend = "decreasing"
        else:
            trend = "fluctuating"
        
        return {
            "dataset": dataset_name,
            "trend": trend,
            "increases": increasing,
            "decreases": decreasing,
            "total_changes": total_changes
        }


def main():
    """Run the data analysis agent with example data."""
    agent = DataAnalysisAgent()
    
    # Example datasets
    sales_data = [100, 150, 120, 180, 200, 190, 220, 250, 240, 280]
    temperature_data = [22.5, 23.1, 21.8, 24.3, 23.7, 22.9, 23.5, 24.1]
    scores_data = [85, 90, 78, 92, 88, 95, 82, 89, 91, 87]
    
    # Load datasets
    agent.load_data("sales", sales_data)
    agent.load_data("temperature", temperature_data)
    agent.load_data("scores", scores_data)
    
    # Print summary
    print(agent.get_summary())
    
    # Analyze sales data
    print("Sales Analysis:")
    import json
    analysis = agent.analyze("sales")
    print(json.dumps(analysis, indent=2))
    print()
    
    # Find trends
    print("Sales Trends:")
    trends = agent.find_trends("sales")
    print(json.dumps(trends, indent=2))
    print()
    
    # Detect outliers
    print("Temperature Outliers (threshold=1.5):")
    outliers = agent.detect_outliers("temperature", threshold=1.5)
    print(f"Found {len(outliers)} outliers: {outliers}")
    print()
    
    # Compare datasets
    print("Compare Sales vs Scores:")
    comparison = agent.compare("sales", "scores")
    print(json.dumps(comparison, indent=2))


if __name__ == "__main__":
    main()
