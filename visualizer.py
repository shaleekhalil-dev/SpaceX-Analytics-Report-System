import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def create_visualizations():
    # تحميل البيانات
    df = pd.read_csv('data/synthetic_spacex_data.csv')
    
    # تحديد التنسيق العام للرسوم
    sns.set_theme(style="whitegrid")
    
    # الرسم الأول: نسبة النجاح حسب نوع المدار
    plt.figure(figsize=(10, 6))
    orbit_success = df.groupby('Orbit')['Outcome'].mean().reset_index()
    sns.barplot(x='Orbit', y='Outcome', data=orbit_success, palette='viridis')
    plt.title('Landing Success Rate by Orbit Type')
    plt.ylabel('Success Rate (0 to 1)')
    plt.xlabel('Orbit')
    plt.savefig('figures/orbit_success_rate.png')
    plt.close()
    
    # الرسم الثاني: العلاقة بين كتلة الحمولة ونتيجة الهبوط
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='Outcome', y='PayloadMass', data=df, palette='Set2')
    plt.title('Payload Mass vs Landing Outcome')
    plt.xlabel('Outcome (0: Failure, 1: Success)')
    plt.ylabel('Payload Mass (kg)')
    plt.savefig('figures/payload_vs_outcome.png')
    plt.close()
    
    print("Visualizations created successfully in figures/ folder.")

if __name__ == "__main__":
    create_visualizations()