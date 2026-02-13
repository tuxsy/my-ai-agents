"""
Code Assistant Agent
An agent that helps with code analysis and suggestions.
"""

import re
from typing import List, Dict, Any, Optional


class CodeAssistantAgent:
    """Agent that assists with code analysis and suggestions."""
    
    def __init__(self, name="CodeAssistant"):
        self.name = name
        self.code_snippets: Dict[str, str] = {}
    
    def add_snippet(self, name: str, code: str):
        """Store a code snippet for analysis."""
        self.code_snippets[name] = code
        print(f"[{self.name}] Added code snippet: {name}")
    
    def count_lines(self, snippet_name: str) -> Dict[str, Any]:
        """Count lines of code in a snippet."""
        if snippet_name not in self.code_snippets:
            return {"error": f"Snippet '{snippet_name}' not found"}
        
        code = self.code_snippets[snippet_name]
        lines = code.split('\n')
        
        total_lines = len(lines)
        blank_lines = sum(1 for line in lines if line.strip() == '')
        comment_lines = sum(1 for line in lines if line.strip().startswith('#'))
        code_lines = total_lines - blank_lines - comment_lines
        
        return {
            "snippet": snippet_name,
            "total_lines": total_lines,
            "code_lines": code_lines,
            "blank_lines": blank_lines,
            "comment_lines": comment_lines
        }
    
    def find_functions(self, snippet_name: str) -> List[str]:
        """Find function definitions in code."""
        if snippet_name not in self.code_snippets:
            return []
        
        code = self.code_snippets[snippet_name]
        
        # Find Python function definitions
        function_pattern = r'def\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*\('
        functions = re.findall(function_pattern, code)
        
        return functions
    
    def find_classes(self, snippet_name: str) -> List[str]:
        """Find class definitions in code."""
        if snippet_name not in self.code_snippets:
            return []
        
        code = self.code_snippets[snippet_name]
        
        # Find Python class definitions
        class_pattern = r'class\s+([a-zA-Z_][a-zA-Z0-9_]*)'
        classes = re.findall(class_pattern, code)
        
        return classes
    
    def find_imports(self, snippet_name: str) -> Dict[str, List[str]]:
        """Find import statements in code."""
        if snippet_name not in self.code_snippets:
            return {"error": f"Snippet '{snippet_name}' not found"}
        
        code = self.code_snippets[snippet_name]
        
        # Find import statements
        import_pattern = r'import\s+([a-zA-Z0-9_., ]+)'
        from_import_pattern = r'from\s+([a-zA-Z0-9_.]+)\s+import'
        
        imports = re.findall(import_pattern, code)
        from_imports = re.findall(from_import_pattern, code)
        
        return {
            "snippet": snippet_name,
            "imports": imports,
            "from_imports": from_imports
        }
    
    def check_style(self, snippet_name: str) -> Dict[str, Any]:
        """Perform basic style checks on code."""
        if snippet_name not in self.code_snippets:
            return {"error": f"Snippet '{snippet_name}' not found"}
        
        code = self.code_snippets[snippet_name]
        lines = code.split('\n')
        
        issues = []
        
        for i, line in enumerate(lines, 1):
            # Check line length
            if len(line) > 100:
                issues.append(f"Line {i}: Line too long ({len(line)} chars)")
            
            # Check trailing whitespace
            if line.rstrip() != line and line.strip():
                issues.append(f"Line {i}: Trailing whitespace")
            
            # Check multiple spaces
            if '  ' in line and not line.strip().startswith('#'):
                # Allow in comments
                pass
        
        return {
            "snippet": snippet_name,
            "issues": issues,
            "issue_count": len(issues)
        }
    
    def analyze(self, snippet_name: str) -> Dict[str, Any]:
        """Perform comprehensive analysis on a code snippet."""
        if snippet_name not in self.code_snippets:
            return {"error": f"Snippet '{snippet_name}' not found"}
        
        analysis = {
            "snippet": snippet_name,
            "line_counts": self.count_lines(snippet_name),
            "functions": self.find_functions(snippet_name),
            "classes": self.find_classes(snippet_name),
            "imports": self.find_imports(snippet_name),
            "style_check": self.check_style(snippet_name)
        }
        
        return analysis
    
    def suggest_improvements(self, snippet_name: str) -> List[str]:
        """Suggest improvements for code."""
        if snippet_name not in self.code_snippets:
            return ["Error: Snippet not found"]
        
        suggestions = []
        
        # Check if there's a docstring
        code = self.code_snippets[snippet_name]
        if '"""' not in code and "'''" not in code:
            suggestions.append("Consider adding docstrings to document your code")
        
        # Check for functions
        functions = self.find_functions(snippet_name)
        if len(functions) > 5:
            suggestions.append("Consider breaking down into smaller modules")
        
        # Check line count
        line_info = self.count_lines(snippet_name)
        if line_info["code_lines"] > 100:
            suggestions.append("Consider refactoring large code into smaller functions")
        
        # Check for error handling
        if 'try' not in code and 'except' not in code:
            suggestions.append("Consider adding error handling with try/except blocks")
        
        if not suggestions:
            suggestions.append("Code looks good! Keep up the good work.")
        
        return suggestions


def main():
    """Run the code assistant with example code."""
    agent = CodeAssistantAgent()
    
    # Example code snippet
    example_code = '''
import math
import sys

class Calculator:
    """A simple calculator class."""
    
    def add(self, a, b):
        """Add two numbers."""
        return a + b
    
    def multiply(self, a, b):
        """Multiply two numbers."""
        return a * b
    
    def power(self, base, exponent):
        """Calculate power."""
        return math.pow(base, exponent)

def main():
    """Main function."""
    calc = Calculator()
    result = calc.add(5, 3)
    print(f"Result: {result}")

if __name__ == "__main__":
    main()
'''
    
    # Add snippet
    agent.add_snippet("calculator", example_code)
    
    # Perform analysis
    print("\n=== Code Analysis ===\n")
    
    # Line count
    print("Line Count:")
    import json
    line_count = agent.count_lines("calculator")
    print(json.dumps(line_count, indent=2))
    print()
    
    # Find functions and classes
    print("Functions found:", agent.find_functions("calculator"))
    print("Classes found:", agent.find_classes("calculator"))
    print()
    
    # Find imports
    print("Imports:")
    imports = agent.find_imports("calculator")
    print(json.dumps(imports, indent=2))
    print()
    
    # Style check
    print("Style Check:")
    style = agent.check_style("calculator")
    print(f"Issues found: {style['issue_count']}")
    print()
    
    # Suggestions
    print("Improvement Suggestions:")
    suggestions = agent.suggest_improvements("calculator")
    for i, suggestion in enumerate(suggestions, 1):
        print(f"{i}. {suggestion}")


if __name__ == "__main__":
    main()
