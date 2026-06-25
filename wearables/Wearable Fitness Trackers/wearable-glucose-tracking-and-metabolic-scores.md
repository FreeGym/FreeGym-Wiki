# Wearable Glucose Tracking and Metabolic Scores

Wearable glucose tracking should be split into two layers: the raw CGM signal and the interpretation layer built on top of it.

A CGM sensor estimates interstitial glucose, not lab blood glucose, insulin sensitivity, HOMA-IR, OGTT response, HbA1c, or metabolic syndrome status. CGM reviews describe these devices as minimally invasive sensors that measure glucose in interstitial fluid; HOMA-IR is derived from fasting plasma glucose and insulin; and metabolic syndrome definitions include central obesity, blood pressure, triglycerides, HDL cholesterol, and fasting glucose. ([Cengiz and Tamborlane, 2009](https://pubmed.ncbi.nlm.nih.gov/19469670/); [Cappon et al., 2019](https://pmc.ncbi.nlm.nih.gov/articles/PMC6712232/); [Matthews et al., 1985](https://pubmed.ncbi.nlm.nih.gov/3899825/); [Alberti et al., 2009](https://pubmed.ncbi.nlm.nih.gov/19805654/))

That raw interstitial glucose trace is a real biological signal, but it is still a sensor estimate with known limitations, especially at low glucose levels. A 2024 systematic review of 22 studies and 2,294 patients found an average MARD of 9.4% for commercially available CGMs; the authors concluded that current CGMs have adequate accuracy in euglycemia and hyperglycemia, but not enough accuracy in hypoglycemia to treat low-glucose readings as definitive without confirmation. The review reported no financial support and no conflicts of interest. ([Dávila-Ruales et al., 2024](https://journals.sagepub.com/doi/10.1177/20420188241304459))

The verdict is therefore split: raw CGM glucose values and transparent CGM-derived metrics are **include** when they remain clearly labeled as sensor/interstitial glucose with units and thresholds. Proprietary “metabolic scores,” “meal scores,” “metabolic fitness scores,” and non-CGM metabolic-health inferences are **exclude**. The score is not the sensor.

## Bottom-line verdict

- Raw CGM glucose trace: **include**, only as sensor/interstitial glucose data, not as a diagnosis, lab blood glucose value, or broad metabolic-health claim. ([Cengiz and Tamborlane, 2009](https://pubmed.ncbi.nlm.nih.gov/19469670/); [Dávila-Ruales et al., 2024](https://journals.sagepub.com/doi/10.1177/20420188241304459))

- Transparent CGM summaries, such as mean sensor glucose or time above a named threshold: **include**, only when units, threshold, sensor source, and time window survive export. ([Spartano et al., 2025](https://academic.oup.com/jcem/article/110/4/1128/7754867))

- Post-meal CGM curves or incremental glucose area-under-curve: **include**, only when the meal timestamp/context is present and the metric is presented as a glucose response, not as a health grade. ([Merino et al., 2022](https://kclpure.kcl.ac.uk/portal/en/publications/validity-of-continuous-glucose-monitoring-for-categorizing-glycem/))

- Proprietary metabolic scores, meal scores, glucose-zone scores, and metabolic fitness grades: **exclude**. The score is not the sensor. ([Chaudhry et al., 2024](https://www.nature.com/articles/s41598-024-56933-2))

- “Metabolic health” inferred from HRV, temperature, activity, sleep, or heart-rate signals without a glucose sensor: **exclude**. These are indirect correlates, not glucose, insulin, HOMA-IR, OGTT, HbA1c, or metabolic-syndrome measurements. ([Matthews et al., 1985](https://pubmed.ncbi.nlm.nih.gov/3899825/); [Alberti et al., 2009](https://pubmed.ncbi.nlm.nih.gov/19805654/))


## What CGM can measure

A CGM can measure a time series of sensor-estimated interstitial glucose. That supports direct observation of glucose patterns across fasting periods, overnight periods, exercise, and meals. It does not directly measure insulin, C-peptide, HOMA-IR, OGTT response, HbA1c, triglycerides, visceral adiposity, hepatic fat, or metabolic syndrome status. HOMA-IR is calculated from fasting plasma glucose and insulin, and metabolic syndrome definitions rely on a broader cluster of measured cardiometabolic risk factors. ([Cengiz and Tamborlane, 2009](https://pubmed.ncbi.nlm.nih.gov/19469670/); [Matthews et al., 1985](https://pubmed.ncbi.nlm.nih.gov/3899825/); [Alberti et al., 2009](https://pubmed.ncbi.nlm.nih.gov/19805654/))

The raw glucose curve after a meal is a stronger data object than a branded meal score. In a 2022 American Journal of Clinical Nutrition study from ZOE PREDICT 1, 394 participants wore two CGMs simultaneously for up to 14 days while consuming standardized and ad libitum meals. The study found relatively strong agreement between paired devices for postprandial glucose iAUC and meal rankings, including Kendall tau of 0.9 for intrabrand meal rankings and 0.7 for interbrand meal rankings. This supports using raw CGM curves or transparent post-meal metrics as glucose-response metrics; it does not turn any proprietary meal score into a standardized biomarker. The source page lists Zoe Ltd among affiliations, so the findings should be interpreted with that commercial personalized-nutrition context in mind. ([Merino et al., 2022](https://kclpure.kcl.ac.uk/portal/en/publications/validity-of-continuous-glucose-monitoring-for-categorizing-glycem/))

## Accuracy of the raw CGM signal

Modern CGMs are good enough to preserve the raw glucose trace as a useful sensor signal, especially for typical-range and high-range glucose patterns. The 2024 systematic review compared commercially available CGM sensors against venous or arterial reference glucose and concluded that overall and hyperglycemic accuracy were adequate, while hypoglycemic accuracy remained insufficient. The authors also noted heterogeneity in accuracy metrics and reporting protocols, which matters when comparing sensors or exporting data across platforms. ([Dávila-Ruales et al., 2024](https://journals.sagepub.com/doi/10.1177/20420188241304459))

This means a field named `cgm_sensor_glucose_mg_dl` can be included. A field named `blood_glucose_mg_dl` should not be created from CGM data, because CGM is not a direct blood measurement. For export, a field named `hypoglycemia_event` should be excluded unless it is explicitly labeled as an unconfirmed CGM low-glucose flag, because low-range accuracy is the weakest part of the measurement system and downstream users may treat the label as confirmed clinical hypoglycemia. ([Cengiz and Tamborlane, 2009](https://pubmed.ncbi.nlm.nih.gov/19469670/); [Dávila-Ruales et al., 2024](https://journals.sagepub.com/doi/10.1177/20420188241304459))

## Healthy, non-diabetic users

The sensor can measure glucose in people without diabetes, but interpretation is not settled. In a Framingham Heart Study analysis of community-dwelling adults, normoglycemic participants wore a Dexcom G6 Pro in blinded mode for at least seven complete days. Normoglycemic participants spent 87.0% of time between 70 and 140 mg/dL, more than 15 minutes per day above 180 mg/dL, and about 3 hours per day above 140 mg/dL. Dexcom provided CGMs at a discounted rate; the authors reported no other relevant conflicts apart from unrelated Novo Nordisk investigator-initiated research funding for two authors. ([Spartano et al., 2025](https://academic.oup.com/jcem/article/110/4/1128/7754867))

That finding matters because a glucose spike in a person without diabetes is not automatically a disease signal. A study of expert clinicians interpreting CGM reports from people without diabetes found poor agreement about who should receive clinical follow-up, with Fleiss kappa of 0.36. More than half of experts recommended follow-up for some reports with time above 180 mg/dL above 2%, even when HbA1c and fasting glucose were normal, but there was no clear consensus. The same study reported no clear trends in follow-up recommendations based on mean glucose or glucose management indicator. ([Spartano et al., 2026](https://journals.sagepub.com/doi/10.1177/19322968251315171))

The gap is clear: CGM supports interstitial glucose dynamics. It does not, by itself, support a broad exported label like “metabolic health abnormality.”

## Behavior-change evidence

CGM feedback can modestly improve glycemic outcomes in studied populations, but the evidence is mostly in diabetes or higher-risk groups, not metabolically healthy users. A 2024 systematic review and meta-analysis of randomized trials included 25 trials and 2,996 adults; most studies were in type 2 diabetes, with fewer in type 1 diabetes, gestational diabetes, and obesity. CGM feedback reduced HbA1c by 0.28 percentage points and increased time in range by 7.4 percentage points, but effects on BMI and weight were not significant. Only 4 of 25 studies measured diet change and only 5 measured physical activity. Eleven studies, or 44%, reported CGM-affiliated conflicts of interest; the review authors also reported some consulting relationships, including former consultation to Zoe by one author. ([Richardson et al., 2024](https://pubmed.ncbi.nlm.nih.gov/39716288/))

This supports a narrow claim: CGM feedback can improve some glycemic outcomes in studied populations. It does not support exporting a proprietary “metabolic fitness” number as if it were a validated health endpoint.

## Proprietary metabolic scores

The clearest brand-specific example is Ultrahuman M1’s MetSc. A 2024 Scientific Reports observational study followed 53 non-diabetic and 52 pre-diabetic Indian/South Asian participants for 14 days using Ultrahuman M1 CGM and Fitbit activity metrics. The study reported that MetSc had inverse relationships with HOMA-IR, OGTT, and HbA1c markers. ([Chaudhry et al., 2024](https://www.nature.com/articles/s41598-024-56933-2))

That is not enough for inclusion as a standardized exported metric. The study was sponsored by Ultrahuman Healthcare Pvt. Ltd.; all listed authors were affiliated with Ultrahuman Healthcare Private Limited; three authors declared stakeholder interests in Ultrahuman; one author was a full-time Ultrahuman employee during the study and analysis period; and the MetSc algorithm is a product-specific proprietary digital score. The study is short, observational, brand-sponsored, product-specific, and not an outcomes validation. ([Chaudhry et al., 2024](https://www.nature.com/articles/s41598-024-56933-2))

The verdict for `metabolic_score`, `meal_score`, `metabolic_fitness_score`, and branded `glucose_zone_score` is **exclude**.

## Non-CGM metabolic-health features

A watch or ring that uses HRV, temperature, heart rate, sleep, and activity can measure or estimate those signals. It cannot directly measure glucose, insulin, HOMA-IR, OGTT response, HbA1c, triglycerides, HDL cholesterol, blood pressure, waist circumference, or metabolic syndrome status. That matters because HOMA-IR is derived from fasting glucose and insulin, and metabolic syndrome is defined using a cluster of measured cardiometabolic risk factors including central obesity, blood pressure, triglycerides, HDL cholesterol, and fasting glucose. ([Matthews et al., 1985](https://pubmed.ncbi.nlm.nih.gov/3899825/); [Alberti et al., 2009](https://pubmed.ncbi.nlm.nih.gov/19805654/))

The mechanistic chain is too long: autonomic and activity signals may correlate with metabolic risk, but correlation is not measurement. Without a glucose sensor or biochemical measurement, a non-CGM wearable metabolic-health feature is an indirect model, not a glucose or insulin-resistance measurement. ([Cappon et al., 2019](https://pmc.ncbi.nlm.nih.gov/articles/PMC6712232/); [Matthews et al., 1985](https://pubmed.ncbi.nlm.nih.gov/3899825/))

The verdict for non-CGM metabolic-health inference is **exclude**.

## Metric verdict table

|Metric|Verdict|Why|
|---|--:|---|
|`cgm_sensor_glucose_mg_dl` or `cgm_sensor_glucose_mmol_l`, timestamped, sensor identified|**Include**|Direct CGM sensor signal; supported for typical and high glucose ranges, but must not be renamed as lab blood glucose. ([Cengiz and Tamborlane, 2009](https://pubmed.ncbi.nlm.nih.gov/19469670/); [Dávila-Ruales et al., 2024](https://journals.sagepub.com/doi/10.1177/20420188241304459))|
|`cgm_glucose_trend_direction` from serial CGM readings|**Include**|A transparent trend from the time series; use as directionality, not diagnosis. ([Dávila-Ruales et al., 2024](https://journals.sagepub.com/doi/10.1177/20420188241304459))|
|`mean_sensor_glucose_mg_dl_24h`|**Include**|Transparent summary of the raw CGM signal, provided the time window and units survive export. ([Spartano et al., 2025](https://academic.oup.com/jcem/article/110/4/1128/7754867))|
|`time_above_140_mg_dl_pct_24h`, `time_above_180_mg_dl_pct_24h`, `time_70_140_mg_dl_pct_24h`|**Include**|Transparent threshold metrics; the threshold, unit, and time window must be in the field name. ([Spartano et al., 2025](https://academic.oup.com/jcem/article/110/4/1128/7754867))|
|`post_meal_glucose_iAUC_0_2h_mg_dl_min` with verified meal timestamp|**Include**|Direct postprandial glucose response; paired-device evidence supports CGM use for meal-response characterization. ([Merino et al., 2022](https://kclpure.kcl.ac.uk/portal/en/publications/validity-of-continuous-glucose-monitoring-for-categorizing-glycem/))|
|`meal_response` without meal timestamp, food amount, or timing context|**Exclude**|Context-dependent metric that becomes misleading once exported. Postprandial CGM interpretation depends on the timing and definition of the meal response. ([Merino et al., 2022](https://kclpure.kcl.ac.uk/portal/en/publications/validity-of-continuous-glucose-monitoring-for-categorizing-glycem/))|
|`hypoglycemia_event` from consumer CGM alone|**Exclude**|Low-range CGM accuracy is weaker; downstream systems may treat the label as confirmed clinical hypoglycemia rather than an unconfirmed sensor flag. ([Dávila-Ruales et al., 2024](https://journals.sagepub.com/doi/10.1177/20420188241304459))|
|`glucose_management_indicator` or CGM-derived estimated HbA1c in people without diabetes|**Exclude**|Expert interpretation in non-diabetic CGM reports is discordant, and follow-up decisions did not show clear trends based on mean glucose or GMI. ([Spartano et al., 2026](https://journals.sagepub.com/doi/10.1177/19322968251315171))|
|`meal_score`, `metabolic_score`, `metabolic_fitness_score`, `glucose_zone_score`|**Exclude**|Proprietary composites with unclear weighting and insufficient independent outcomes validation. ([Chaudhry et al., 2024](https://www.nature.com/articles/s41598-024-56933-2))|
|`metabolic_health_from_hrv_temperature_activity`|**Exclude**|No direct glucose, insulin, HOMA-IR, OGTT, HbA1c, or metabolic-syndrome measurement. ([Matthews et al., 1985](https://pubmed.ncbi.nlm.nih.gov/3899825/); [Alberti et al., 2009](https://pubmed.ncbi.nlm.nih.gov/19805654/))|
|`insulin_resistance_score` from watch/ring data alone|**Exclude**|HOMA-IR is a biochemical construct derived from fasting glucose and insulin; wearable-only inference is not a validated direct measure. ([Matthews et al., 1985](https://pubmed.ncbi.nlm.nih.gov/3899825/))|

## Practical interpretation

The raw glucose curve is the useful object. If a CGM shows that a person’s glucose rose after a specific meal, fell after exercise, or stayed higher overnight, that is observable sensor data. The correct exported metric is the glucose trace or a transparent transformation of that trace, with sensor type, units, thresholds, and time window intact. ([Cengiz and Tamborlane, 2009](https://pubmed.ncbi.nlm.nih.gov/19469670/); [Dávila-Ruales et al., 2024](https://journals.sagepub.com/doi/10.1177/20420188241304459); [Merino et al., 2022](https://kclpure.kcl.ac.uk/portal/en/publications/validity-of-continuous-glucose-monitoring-for-categorizing-glycem/))

The branded score is not the useful object. A “meal score of 7.2” or “metabolic fitness score of 84” compresses the raw curve into a proprietary value with unclear thresholds, unclear weighting, unclear population calibration, and insufficient independent outcomes validation. That score should not enter a data pipeline as if it were a standardized biomarker. ([Chaudhry et al., 2024](https://www.nature.com/articles/s41598-024-56933-2))

The marketing inflation is the finding: CGM supports glucose dynamics, not whole-body metabolic health. Non-CGM wearables support heart-rate, HRV, sleep, temperature, and activity patterns, not glucose tracking. A product can help users notice habits, but habit feedback is not the same as a validated metabolic-health metric. ([Cappon et al., 2019](https://pmc.ncbi.nlm.nih.gov/articles/PMC6712232/); [Matthews et al., 1985](https://pubmed.ncbi.nlm.nih.gov/3899825/); [Alberti et al., 2009](https://pubmed.ncbi.nlm.nih.gov/19805654/); [Richardson et al., 2024](https://pubmed.ncbi.nlm.nih.gov/39716288/))

## References

- Dávila-Ruales V, Gilón LF, Gómez AM, Muñoz OM, Serrano MN, Henao DC. [Evaluating the precision and reliability of real-time continuous glucose monitoring systems in ambulatory settings: a systematic review](https://journals.sagepub.com/doi/10.1177/20420188241304459). Therapeutic Advances in Endocrinology and Metabolism. 2024. DOI: 10.1177/20420188241304459.

- Cengiz E, Tamborlane WV. [A Tale of Two Compartments: Interstitial Versus Blood Glucose Monitoring](https://pubmed.ncbi.nlm.nih.gov/19469670/). Diabetes Technology & Therapeutics. 2009;11 Suppl 1:S11-S16. DOI: 10.1089/dia.2009.0002. PMID: 19469670.

- Cappon G, Vettoretti M, Sparacino G, Facchinetti A. [Continuous Glucose Monitoring Sensors for Diabetes Management: A Review of Technologies and Applications](https://pmc.ncbi.nlm.nih.gov/articles/PMC6712232/). Diabetes Metab J. 2019;43(4):383-397. DOI: 10.4093/dmj.2019.0121. PMID: 31441246.

- Matthews DR, Hosker JP, Rudenski AS, Naylor BA, Treacher DF, Turner RC. [Homeostasis model assessment: insulin resistance and beta-cell function from fasting plasma glucose and insulin concentrations in man](https://pubmed.ncbi.nlm.nih.gov/3899825/). Diabetologia. 1985;28(7):412-419. DOI: 10.1007/BF00280883. PMID: 3899825.

- Alberti KGMM, Eckel RH, Grundy SM, et al. [Harmonizing the metabolic syndrome: a joint interim statement of the International Diabetes Federation Task Force on Epidemiology and Prevention; National Heart, Lung, and Blood Institute; American Heart Association; World Heart Federation; International Atherosclerosis Society; and International Association for the Study of Obesity](https://pubmed.ncbi.nlm.nih.gov/19805654/). Circulation. 2009;120(16):1640-1645. DOI: 10.1161/CIRCULATIONAHA.109.192644. PMID: 19805654.

- Merino J, Linenberg I, Bermingham KM, et al. [Validity of continuous glucose monitoring for categorizing glycemic responses to diet: implications for use in personalized nutrition](https://kclpure.kcl.ac.uk/portal/en/publications/validity-of-continuous-glucose-monitoring-for-categorizing-glycem/). American Journal of Clinical Nutrition. 2022;115(6):1569-1576. DOI: 10.1093/ajcn/nqac026.

- Richardson KM, Jospe MR, Bohlen LC, Crawshaw J, Saleh AA, Schembre SM. [The efficacy of using continuous glucose monitoring as a behaviour change tool in populations with and without diabetes: a systematic review and meta-analysis of randomised controlled trials](https://pubmed.ncbi.nlm.nih.gov/39716288/). International Journal of Behavioral Nutrition and Physical Activity. 2024;21(1):145. DOI: 10.1186/s12966-024-01692-6. PMID: 39716288.

- Spartano NL, Sultana N, Lin H, et al. [Defining Continuous Glucose Monitor Time in Range in a Large Community-Based Cohort Without Diabetes](https://academic.oup.com/jcem/article/110/4/1128/7754867). Journal of Clinical Endocrinology and Metabolism. 2025;110(4):1128-1134. DOI: 10.1210/clinem/dgae626.

- Spartano NL, Prescott B, Walker ME, et al. [Expert Clinical Interpretation of Continuous Glucose Monitor Reports From Individuals Without Diabetes](https://journals.sagepub.com/doi/10.1177/19322968251315171). Journal of Diabetes Science and Technology. 2026;20(3). DOI: 10.1177/19322968251315171.

- Chaudhry M, Kumar M, Singhal V, Srinivasan B. [Metabolic health tracking using Ultrahuman M1 continuous glucose monitoring platform in non- and pre-diabetic Indians: a multi-armed observational study](https://www.nature.com/articles/s41598-024-56933-2). Scientific Reports. 2024;14:6490. DOI: 10.1038/s41598-024-56933-2.