import pandas as pd
from ydata_profiling import ProfileReport

# Load detections data
df = pd.read_csv("detections.csv")

# Generate AutoEDA report
profile = ProfileReport(
    df,
    title="Helmet Detection – AutoEDA Report",
    explorative=True
)

# Save report
profile.to_file("helmet_autoeda.html")

print("AutoEDA report generated: helmet_autoeda.html")
