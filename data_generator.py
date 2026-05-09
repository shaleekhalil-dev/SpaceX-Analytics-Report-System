import pandas as pd
import numpy as np

def generate_spacex_data(n_samples=100):
    np.random.seed(42)
    
    data = {
        'FlightNumber': range(1, n_samples + 1),
        'PayloadMass': np.random.randint(500, 15000, size=n_samples),
        'Orbit': np.random.choice(['LEO', 'VLEO', 'GTO', 'SSO', 'ISS'], size=n_samples),
        'LaunchSite': np.random.choice(['CCAFS SLC 40', 'KSC LC 39A', 'VAFB SLC 4E'], size=n_samples),
        'LandingPad': np.random.choice(['OCISLY', 'JRTI', 'LZ-1', 'LZ-4'], size=n_samples),
        'Outcome': np.random.choice([1, 0], size=n_samples, p=[0.7, 0.3])
    }
    
    df = pd.DataFrame(data)
    df.to_csv('data/synthetic_spacex_data.csv', index=False)
    print("Synthetic data generated successfully in data/ folder.")

if __name__ == "__main__":
    generate_spacex_data()