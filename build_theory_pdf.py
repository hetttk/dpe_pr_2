from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table,
                                 TableStyle, PageBreak, ListFlowable, ListItem)

doc = SimpleDocTemplate("report/Data_Cleanser_Theory.pdf", pagesize=letter,
                         topMargin=0.75*inch, bottomMargin=0.75*inch,
                         leftMargin=0.75*inch, rightMargin=0.75*inch)

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name="H1c", parent=styles["Heading1"], spaceAfter=10, textColor=colors.HexColor("#1F3864")))
styles.add(ParagraphStyle(name="H2c", parent=styles["Heading2"], spaceBefore=14, spaceAfter=6, textColor=colors.HexColor("#2E5395")))
styles.add(ParagraphStyle(name="H3c", parent=styles["Heading3"], spaceBefore=8, spaceAfter=4, textColor=colors.HexColor("#44546A")))
styles.add(ParagraphStyle(name="Bodyc", parent=styles["BodyText"], spaceAfter=8, leading=14))
styles.add(ParagraphStyle(name="Small", parent=styles["BodyText"], fontSize=9, textColor=colors.grey))

story = []

story.append(Paragraph("PR. 2 — Data Cleanser", styles["Title"]))
story.append(Paragraph("Theory Concepts &amp; Definitions", styles["H1c"]))
story.append(Paragraph(
    "Missing Value Imputation and Outlier Handling for Healthcare Data Preprocessing",
    styles["Bodyc"]))
story.append(Spacer(1, 12))

story.append(Paragraph("1. Missing Value Imputation", styles["H1c"]))

story.append(Paragraph("1.1 Simple Imputer", styles["H2c"]))
story.append(Paragraph(
    "Replaces every missing value in a column with a single summary statistic computed "
    "from the observed (non-missing) values of that column. For numerical columns the "
    "statistic is typically the <b>mean</b> or <b>median</b>; for categorical columns it "
    "is the <b>most frequent value (mode)</b>. It is the simplest and fastest imputation "
    "technique, but because it inserts the same repeated value into every gap, it "
    "artificially reduces the column's variance and can distort its distribution shape.",
    styles["Bodyc"]))

story.append(Paragraph("1.2 Most Frequent Imputation", styles["H2c"]))
story.append(Paragraph(
    "A special case of Simple Imputer used for categorical data: every missing entry is "
    "replaced with the category that occurs most often in the column. It is easy to apply "
    "and keeps the column fully valid (no new categories introduced), but it can "
    "over-represent the majority class if a large share of values were missing.",
    styles["Bodyc"]))

story.append(Paragraph("1.3 Missing Indicator + Random Sample Imputation", styles["H2c"]))
story.append(Paragraph(
    "A two-part technique. First, a <b>Missing Indicator</b> creates a new binary (0/1) "
    "column that flags exactly which rows originally had a missing value in a given "
    "column — this preserves the possibility that <i>missingness itself</i> is "
    "informative (e.g. a lab test wasn't ordered). Second, <b>Random Sample Imputation</b> "
    "fills each gap by drawing a real, randomly-selected value from the column's own "
    "observed data (with replacement), rather than inserting one fixed number. This keeps "
    "the post-imputation distribution's shape and variance much closer to the original "
    "than mean/median imputation does.",
    styles["Bodyc"]))

story.append(Paragraph("1.4 KNN Imputer (k-Nearest Neighbors)", styles["H2c"]))
story.append(Paragraph(
    "A multivariate imputation method. For a row with a missing value, KNN Imputer finds "
    "the <i>k</i> most similar rows (by distance across the other numeric columns) and "
    "fills the gap using a (distance-weighted) average of those neighbors' values in the "
    "target column. Because it uses relationships between variables rather than a single "
    "column statistic, it typically produces more realistic estimates — at the cost of "
    "higher computation time and sensitivity to unscaled features or unresolved outliers.",
    styles["Bodyc"]))

story.append(Paragraph("1.5 MICE (Multivariate Imputation by Chained Equations)", styles["H2c"]))
story.append(Paragraph(
    "The most sophisticated method covered here (implemented as <b>IterativeImputer</b> "
    "in scikit-learn). Each column with missing values is modeled as a regression problem, "
    "predicted from all other columns. The algorithm cycles through every column "
    "repeatedly (\"chained equations\"), refining the imputed values each pass until they "
    "stabilize. MICE generally gives the least-biased estimates for data that is Missing "
    "At Random (MAR), since it explicitly captures the conditional relationships between "
    "variables, but it is also the slowest and least transparent method to explain.",
    styles["Bodyc"]))

story.append(Paragraph("2. Outlier Detection and Treatment", styles["H1c"]))

story.append(Paragraph("2.1 Z-score Method", styles["H2c"]))
story.append(Paragraph(
    "Measures how many standard deviations a value sits from its column's mean: "
    "<i>z = (x - mean) / std</i>. A common threshold flags any point with |z| &gt; 3 as an "
    "outlier, since under a roughly normal distribution only about 0.3% of points should "
    "naturally fall that far out. It is simple and fast, but assumes the data is close to "
    "normally distributed, and the mean/std it relies on can themselves be skewed by the "
    "very outliers it's trying to detect.",
    styles["Bodyc"]))

story.append(Paragraph("2.2 IQR (Interquartile Range) Method", styles["H2c"]))
story.append(Paragraph(
    "Measures spread using the middle 50% of the data: <i>IQR = Q3 - Q1</i> (the "
    "difference between the 75th and 25th percentiles). Any value below "
    "<i>Q1 - 1.5&times;IQR</i> or above <i>Q3 + 1.5&times;IQR</i> is flagged as an "
    "outlier. Because it is based on quantiles rather than the mean, it is a more "
    "\"robust\" statistic — much less sensitive to the outliers themselves than the "
    "Z-score method, and generally preferred for skewed distributions. This is the same "
    "rule that determines the whiskers on a standard boxplot.",
    styles["Bodyc"]))

story.append(Paragraph("2.3 Percentile Method (Percentile Capping)", styles["H2c"]))
story.append(Paragraph(
    "Sets fixed cutoffs at chosen percentiles of the data — commonly the 1st and 99th "
    "percentile — and <b>caps (clips)</b> any value beyond those bounds to the cutoff "
    "itself, rather than deleting the row. This guarantees a predictable, reproducible "
    "proportion of the data sits at each tail regardless of the column's underlying shape.",
    styles["Bodyc"]))

story.append(Paragraph("2.4 Winsorization", styles["H2c"]))
story.append(Paragraph(
    "Conceptually similar to percentile capping: extreme values beyond a chosen "
    "percentile threshold (e.g. the bottom and top 1%) are replaced with the nearest "
    "boundary value rather than removed. The key advantage over deleting outlier rows is "
    "that the full sample size is preserved — no data (and no information contained in a "
    "row's other columns) is thrown away, which is especially valuable for smaller or "
    "clinically important datasets.",
    styles["Bodyc"]))

story.append(Paragraph("3. Method Comparison Summary", styles["H1c"]))

data = [
    ["Category", "Method", "Best Suited For", "Key Tradeoff"],
    ["Missing\nValues", "Simple Imputer\n(mean/median/mode)",
     "Quick baseline, low-missingness columns",
     "Reduces variance; distorts distribution shape"],
    ["", "Most Frequent",
     "Categorical columns", "Over-represents majority class"],
    ["", "Missing Indicator +\nRandom Sample",
     "When missingness itself may\nbe informative",
     "Preserves distribution shape well;\nadds extra columns"],
    ["", "KNN Imputer",
     "Numeric data with correlated\nfeatures",
     "More accurate; computationally heavier"],
    ["", "MICE",
     "Data Missing At Random (MAR)\nwith multiple correlated columns",
     "Most accurate; slowest, least transparent"],
    ["Outliers", "Z-score",
     "Roughly normal distributions",
     "Sensitive to the outliers it detects"],
    ["", "IQR",
     "Skewed distributions (robust)",
     "Fixed multiplier (1.5) may not fit every column"],
    ["", "Percentile Capping",
     "Predictable, reproducible bounds",
     "Not adaptive to actual distribution shape"],
    ["", "Winsorization",
     "Preserving full sample size",
     "Still shrinks true extreme values toward center"],
]

tbl = Table(data, colWidths=[0.75*inch, 1.35*inch, 1.9*inch, 2.1*inch], repeatRows=1)
tbl.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#1F3864")),
    ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
    ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
    ("FONTSIZE", (0, 0), (-1, -1), 8),
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#B0B0B0")),
    ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#F2F5FA")]),
    ("SPAN", (0, 1), (0, 5)),
    ("SPAN", (0, 6), (0, 9)),
    ("TOPPADDING", (0, 0), (-1, -1), 5),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
]))
story.append(tbl)

story.append(Spacer(1, 14))
story.append(Paragraph(
    "Note: This document summarizes the theory behind the techniques applied in "
    "<i>Data_Cleanser.ipynb</i>. All definitions and comparisons reflect standard "
    "data-preprocessing practice as used in the accompanying notebook.",
    styles["Small"]))

doc.build(story)
print("PDF built.")
