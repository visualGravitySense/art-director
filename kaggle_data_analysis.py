#!/usr/bin/env python3
"""
ART DIRECTOR Website - Kaggle Dataset Analysis Script
This script demonstrates how to analyze design-related datasets for your portfolio website.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from datetime import datetime
import json

class ArtDirectorDataAnalyzer:
    """
    A class to analyze design and art datasets for ART DIRECTOR website insights.
    """
    
    def __init__(self):
        self.datasets = {}
        self.insights = {}
        
    def load_sample_data(self):
        """
        Load sample data for demonstration purposes.
        In production, this would load actual Kaggle datasets.
        """
        # Sample color psychology data
        color_data = {
            'color': ['Red', 'Blue', 'Green', 'Yellow', 'Purple', 'Orange', 'Black', 'White'],
            'energy_level': [8, 6, 7, 9, 5, 8, 3, 4],
            'trust_level': [4, 9, 8, 6, 7, 5, 8, 9],
            'creativity_score': [7, 8, 6, 9, 8, 7, 6, 5],
            'conversion_rate': [0.12, 0.15, 0.13, 0.11, 0.14, 0.13, 0.16, 0.14]
        }
        
        # Sample design trend data
        trend_data = {
            'year': [2020, 2021, 2022, 2023, 2024],
            'minimalism': [0.3, 0.35, 0.4, 0.45, 0.5],
            'brutalism': [0.1, 0.15, 0.2, 0.25, 0.3],
            'neomorphism': [0.2, 0.25, 0.3, 0.2, 0.15],
            'glassmorphism': [0.1, 0.2, 0.25, 0.3, 0.25]
        }
        
        # Sample portfolio performance data
        portfolio_data = {
            'project_type': ['Logo Design', 'Web Design', 'Brand Identity', 'UI/UX', 'Print Design'],
            'avg_price': [500, 2500, 3000, 4000, 800],
            'completion_time': [3, 14, 21, 28, 5],
            'client_satisfaction': [4.2, 4.5, 4.7, 4.6, 4.3],
            'repeat_clients': [0.3, 0.4, 0.5, 0.45, 0.35]
        }
        
        self.datasets['color_psychology'] = pd.DataFrame(color_data)
        self.datasets['design_trends'] = pd.DataFrame(trend_data)
        self.datasets['portfolio_performance'] = pd.DataFrame(portfolio_data)
        
        print("✅ Sample datasets loaded successfully!")
        
    def analyze_color_psychology(self):
        """
        Analyze color psychology data to understand color effectiveness.
        """
        df = self.datasets['color_psychology']
        
        # Find most effective colors for different purposes
        best_energy = df.loc[df['energy_level'].idxmax(), 'color']
        best_trust = df.loc[df['trust_level'].idxmax(), 'color']
        best_creativity = df.loc[df['creativity_score'].idxmax(), 'color']
        best_conversion = df.loc[df['conversion_rate'].idxmax(), 'color']
        
        insights = {
            'best_energy_color': best_energy,
            'best_trust_color': best_trust,
            'best_creativity_color': best_creativity,
            'best_conversion_color': best_conversion,
            'color_analysis': df.to_dict('records')
        }
        
        self.insights['color_psychology'] = insights
        print(f"🎨 Color Analysis Complete:")
        print(f"   Best for Energy: {best_energy}")
        print(f"   Best for Trust: {best_trust}")
        print(f"   Best for Creativity: {best_creativity}")
        print(f"   Best for Conversion: {best_conversion}")
        
        return insights
    
    def analyze_design_trends(self):
        """
        Analyze design trend evolution over time.
        """
        df = self.datasets['design_trends']
        
        # Calculate trend growth rates
        trends = ['minimalism', 'brutalism', 'neomorphism', 'glassmorphism']
        growth_rates = {}
        
        for trend in trends:
            start_value = df[trend].iloc[0]
            end_value = df[trend].iloc[-1]
            growth_rate = ((end_value - start_value) / start_value) * 100
            growth_rates[trend] = growth_rate
        
        # Find fastest growing trend
        fastest_growing = max(growth_rates, key=growth_rates.get)
        
        insights = {
            'fastest_growing_trend': fastest_growing,
            'growth_rate': growth_rates[fastest_growing],
            'all_growth_rates': growth_rates,
            'trend_data': df.to_dict('records')
        }
        
        self.insights['design_trends'] = insights
        print(f"📈 Design Trend Analysis Complete:")
        print(f"   Fastest Growing Trend: {fastest_growing} ({growth_rates[fastest_growing]:.1f}% growth)")
        
        return insights
    
    def analyze_portfolio_performance(self):
        """
        Analyze portfolio performance metrics.
        """
        df = self.datasets['portfolio_performance']
        
        # Find most profitable project type
        df['profitability'] = df['avg_price'] / df['completion_time']
        most_profitable = df.loc[df['profitability'].idxmax(), 'project_type']
        
        # Find highest satisfaction project
        highest_satisfaction = df.loc[df['client_satisfaction'].idxmax(), 'project_type']
        
        # Find best for repeat business
        best_repeat = df.loc[df['repeat_clients'].idxmax(), 'project_type']
        
        insights = {
            'most_profitable': most_profitable,
            'highest_satisfaction': highest_satisfaction,
            'best_repeat_business': best_repeat,
            'performance_data': df.to_dict('records')
        }
        
        self.insights['portfolio_performance'] = insights
        print(f"💰 Portfolio Performance Analysis Complete:")
        print(f"   Most Profitable: {most_profitable}")
        print(f"   Highest Satisfaction: {highest_satisfaction}")
        print(f"   Best for Repeat Business: {best_repeat}")
        
        return insights
    
    def create_visualizations(self):
        """
        Create visualizations for the website.
        """
        # Set up the plotting style
        plt.style.use('seaborn-v0_8')
        fig, axes = plt.subplots(2, 2, figsize=(15, 12))
        fig.suptitle('ART DIRECTOR Data Insights Dashboard', fontsize=16, fontweight='bold')
        
        # Color Psychology Chart
        df_color = self.datasets['color_psychology']
        axes[0, 0].bar(df_color['color'], df_color['conversion_rate'], color=df_color['color'].str.lower())
        axes[0, 0].set_title('Color Conversion Rates')
        axes[0, 0].set_ylabel('Conversion Rate')
        axes[0, 0].tick_params(axis='x', rotation=45)
        
        # Design Trends Chart
        df_trends = self.datasets['design_trends']
        for trend in ['minimalism', 'brutalism', 'neomorphism', 'glassmorphism']:
            axes[0, 1].plot(df_trends['year'], df_trends[trend], marker='o', label=trend)
        axes[0, 1].set_title('Design Trend Evolution')
        axes[0, 1].set_xlabel('Year')
        axes[0, 1].set_ylabel('Popularity')
        axes[0, 1].legend()
        
        # Portfolio Performance Chart
        df_portfolio = self.datasets['portfolio_performance']
        axes[1, 0].scatter(df_portfolio['avg_price'], df_portfolio['client_satisfaction'], 
                          s=df_portfolio['repeat_clients']*100, alpha=0.7)
        axes[1, 0].set_title('Portfolio Performance: Price vs Satisfaction')
        axes[1, 0].set_xlabel('Average Price ($)')
        axes[1, 0].set_ylabel('Client Satisfaction')
        
        # Color Energy vs Trust
        axes[1, 1].scatter(df_color['energy_level'], df_color['trust_level'], 
                          c=df_color['conversion_rate'], cmap='viridis', s=100)
        axes[1, 1].set_title('Color Psychology: Energy vs Trust')
        axes[1, 1].set_xlabel('Energy Level')
        axes[1, 1].set_ylabel('Trust Level')
        
        plt.tight_layout()
        plt.savefig('art_director_insights.png', dpi=300, bbox_inches='tight')
        print("📊 Visualizations saved as 'art_director_insights.png'")
        
    def generate_website_insights(self):
        """
        Generate insights specifically for website development.
        """
        insights = {
            'recommended_colors': {
                'primary': self.insights['color_psychology']['best_conversion_color'],
                'secondary': self.insights['color_psychology']['best_trust_color'],
                'accent': self.insights['color_psychology']['best_creativity_color']
            },
            'design_direction': {
                'trend_focus': self.insights['design_trends']['fastest_growing_trend'],
                'growth_potential': self.insights['design_trends']['growth_rate']
            },
            'service_recommendations': {
                'focus_service': self.insights['portfolio_performance']['most_profitable'],
                'satisfaction_leader': self.insights['portfolio_performance']['highest_satisfaction']
            },
            'generated_at': datetime.now().isoformat()
        }
        
        # Save insights to JSON file
        with open('website_insights.json', 'w') as f:
            json.dump(insights, f, indent=2)
        
        print("💡 Website insights generated and saved to 'website_insights.json'")
        return insights
    
    def run_complete_analysis(self):
        """
        Run the complete analysis pipeline.
        """
        print("🚀 Starting ART DIRECTOR Data Analysis...")
        print("=" * 50)
        
        # Load data
        self.load_sample_data()
        
        # Run analyses
        self.analyze_color_psychology()
        self.analyze_design_trends()
        self.analyze_portfolio_performance()
        
        # Create visualizations
        self.create_visualizations()
        
        # Generate website insights
        insights = self.generate_website_insights()
        
        print("=" * 50)
        print("✅ Analysis Complete!")
        print("\n🎯 Key Recommendations for Your Website:")
        print(f"   Primary Color: {insights['recommended_colors']['primary']}")
        print(f"   Design Trend Focus: {insights['design_direction']['trend_focus']}")
        print(f"   Service Focus: {insights['service_recommendations']['focus_service']}")
        
        return insights

def main():
    """
    Main function to run the analysis.
    """
    analyzer = ArtDirectorDataAnalyzer()
    insights = analyzer.run_complete_analysis()
    
    print("\n📁 Files Generated:")
    print("   - art_director_insights.png (visualizations)")
    print("   - website_insights.json (data insights)")
    
    print("\n🎨 Next Steps:")
    print("   1. Review the generated insights")
    print("   2. Integrate findings into your website design")
    print("   3. Set up Kaggle API for real data")
    print("   4. Build interactive data visualizations")

if __name__ == "__main__":
    main()
