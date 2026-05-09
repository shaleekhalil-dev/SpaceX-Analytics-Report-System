import pandas as pd

def process_data():
    df = pd.read_csv('data/synthetic_spacex_data.csv')
    
    success_rate = df['Outcome'].mean() * 100
    avg_payload = df['PayloadMass'].mean()
    orbit_success = df.groupby('Orbit')['Outcome'].mean() * 100
    site_counts = df['LaunchSite'].value_counts()
    
    summary_report = f"""
    SpaceX Flight Analysis Summary
    ==============================
    Total Number of Flights: {len(df)}
    Overall Landing Success Rate: {success_rate:.2f}%
    Average Payload Mass: {avg_payload:.2f} kg
    
    Success Rate by Orbit Type:
    {orbit_success.to_string()}
    
    Flight Distribution by Launch Site:
    {site_counts.to_string()}
    """
    
    with open('outputs/summary_stats.txt', 'w', encoding='utf-8') as f:
        f.write(summary_report)
    
    print("Data processing complete. Summary report generated in outputs/ folder.")

if __name__ == "__main__":
    process_data()