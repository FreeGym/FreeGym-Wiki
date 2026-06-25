# Body Composition, Biological Age, and Healthspan Scores

For a health-data pipeline that treats exported numbers as objective physiological variables, the practical verdict is straightforward: **exclude these metrics as objective inputs**. Wrist-based body composition is an indirect estimate, and validation evidence shows individual-level error too wide for the small changes users usually care about. Biological age, healthspan, cardiovascular age, and AGEs-style scores should also be excluded as objective variables unless a specific product score has independent validation for the exact exported metric, population, and use case. The sources below support narrower statements about inputs, algorithms, estimates, wellness features, and selected research models; they do not support treating the broad consumer labels as independently validated biological-age or healthspan endpoints. ([MDPI](https://www.mdpi.com/2411-5142/11/1/65), [Frontiers](https://www.frontiersin.org/journals/sports-and-active-living/articles/10.3389/fspor.2025.1644082/full), [Aquila Digital Community](https://aquila.usm.edu/fac_pubs/20489/), [WHOOP](https://www.whoop.com/us/en/thelocker/Healthspan-Data-Meets-Longevity/), [Ultrahuman](https://blog.ultrahuman.com/blog/introducing-ultra-age/), [Oura Support](https://support.ouraring.com/hc/en-us/articles/28451491040019-Cardiovascular-Age), [Samsung Global Newsroom](https://news.samsung.com/global/unlocking-new-possibilities-for-preventative-wellness-with-new-galaxy-watch-and-bioactive-sensor))

## Verdict

- **Wrist-based body fat percentage: exclude.** A 2026 systematic review comparing BIA devices with the four-compartment model found body-fat limits of agreement typically spanning 15 to 20 percentage points, meaning small individual changes are well inside measurement noise. A 2025 Samsung Galaxy Watch5 validation study against DXA reported wearable body-fat limits of agreement from -7.85 to +6.1 percentage points and did not meet equivalence overall. ([MDPI](https://www.mdpi.com/2411-5142/11/1/65), [Frontiers](https://www.frontiersin.org/journals/sports-and-active-living/articles/10.3389/fspor.2025.1644082/full))

- **Wrist-based fat mass, lean mass, skeletal muscle, and body water estimates: exclude.** The same 2025 Galaxy Watch5 study found skeletal muscle percentage did not meet validity thresholds for agreement, error, or equivalence, with wearable skeletal-muscle limits of agreement from -10.65 to -2.27 percentage points. A separate smartwatch-BIA study against a four-compartment model found that no tested device demonstrated equivalence with the four-compartment model. ([Frontiers](https://www.frontiersin.org/journals/sports-and-active-living/articles/10.3389/fspor.2025.1644082/full), [Aquila Digital Community](https://aquila.usm.edu/fac_pubs/20489/))

- **Wrist-BIA trend tracking: exclude.** For objective export, trend inclusion should require independent longitudinal validation showing that the direction of change is reliable under typical-use conditions. The 2026 BIA systematic review excluded longitudinal body-composition-change studies and noted that proprietary equations and inconsistent premeasurement protocols limit interpretation. The smartwatch-BIA study against the four-compartment model also stated that future follow-up testing is needed before using the device to monitor body-composition change over time. ([MDPI](https://www.mdpi.com/2411-5142/11/1/65), [Aquila Digital Community](https://aquila.usm.edu/fac_pubs/20489/))

- **WHOOP Age, WHOOP Healthspan, and Pace of Aging: exclude.** WHOOP describes WHOOP Age as a proxy for physiological age based on sleep, activity, and fitness data, describes Pace of Aging as a weekly indicator of how WHOOP Age is changing, and says Healthspan is for wellness purposes only and not for medical use. That product documentation is useful for identifying the marketed feature, but it is not independent validation sufficient to treat WHOOP Age as a biological-age or healthspan endpoint. ([WHOOP](https://www.whoop.com/us/en/thelocker/Healthspan-Data-Meets-Longevity/))

- **Ultrahuman Ultra Age, Brain Age, Pulse Age, Blood Age, and Speed of Aging: exclude.** Ultrahuman describes Ultra Age as a single insight combining Brain Age, Pulse Age, and Blood Age, with claims about lifestyle, sleep, exercise, nutrition, and aging trajectory. That supports a product-description claim about an age-labeled composite; it does not establish that Ultra Age is a directly measured or independently validated biological-age outcome. ([Ultrahuman](https://blog.ultrahuman.com/blog/introducing-ultra-age/))

- **Oura Cardiovascular Age: exclude as a general-purpose health variable.** Oura states that Cardiovascular Age is an estimate based on estimated pulse wave velocity and heartbeat-signal shape, and that the ring does not directly measure PWV. Oura also says results may not be valid for users with certain medical conditions and that the ring is not a medical device. ([Oura Support](https://support.ouraring.com/hc/en-us/articles/28451491040019-Cardiovascular-Age))

- **Samsung AGEs Index: exclude.** Samsung markets AGEs Index as an indicator of metabolic health and biological aging, measured during sleep, but also frames Galaxy Watch health features as wellness and fitness tools rather than diagnostic or treatment tools. Samsung's AGEs Index footnote states that AGEs Index monitoring is for fitness and wellness only, not for diagnosis or treatment of any medical condition. ([Samsung Global Newsroom](https://news.samsung.com/global/unlocking-new-possibilities-for-preventative-wellness-with-new-galaxy-watch-and-bioactive-sensor))


## What wrist-based BIA actually measures

Bioelectrical impedance analysis does not directly measure fat, muscle, or water compartments. It measures electrical impedance and then uses equations to estimate body composition. The 2026 systematic review notes that BIA devices use proprietary equations and that knowledge about validation methods and cohort demographics is often limited. ([MDPI](https://www.mdpi.com/2411-5142/11/1/65))

This matters because a downstream column label such as "body fat %" or "skeletal muscle" can easily lose the measurement context: "model-estimated body fat from a hydration-sensitive impedance equation." Once that context is stripped, the number can be misread as a ground-truth physiological measure.

## Why the body-composition numbers fail individual tracking

For individual tracking, the strongest issue is not whether the average bias is small. The issue is whether the device can detect meaningful change in one person.

A 2026 systematic review of BIA against the four-compartment model found that mean bias could look modest, but the limits of agreement were wide: body-fat limits of agreement typically spanned 15 to 20 percentage points, and fat-free-mass limits often exceeded +/-6 kg. The authors concluded that BIA was acceptable at the population level but not at the individual level for percentage body fat and fat-free mass. ([MDPI](https://www.mdpi.com/2411-5142/11/1/65))

The consumer smartwatch evidence does not rescue the metric. In a 2025 validation study of Samsung Galaxy Watch5 against DXA in 108 physically active adults, wearable body-fat percentage had strong correlation with DXA, but correlation is not enough for individual tracking. Equivalence was not supported overall, and the body-fat limits of agreement were -7.85 to +6.1 percentage points. Although the female subgroup met the study's equivalence threshold for body-fat percentage, the overall sample did not. Skeletal muscle percentage performed worse, with low concordance and no equivalence. ([Frontiers](https://www.frontiersin.org/journals/sports-and-active-living/articles/10.3389/fspor.2025.1644082/full))

A separate smartwatch-BIA study against a four-compartment model found that no tested device demonstrated equivalence with the four-compartment model, that smartwatch BIA overestimated body fat, and that future research was needed before using the device to monitor body-composition change over time. ([Aquila Digital Community](https://aquila.usm.edu/fac_pubs/20489/))

Against those reported limits of agreement, a week-to-week change of 0.5 percentage points in body fat should be treated as noise, not a finding.

## Measurement conditions make export worse

The Galaxy Watch5 validation study used controlled conditions: participants were told to avoid food, caffeine, and other drinks for 3 hours before testing, and to avoid alcohol, smoking, and heavy exercise for 24 hours. Unless a consumer export records comparable premeasurement conditions, the exported value loses an important part of the validation context. ([Frontiers](https://www.frontiersin.org/journals/sports-and-active-living/articles/10.3389/fspor.2025.1644082/full))

The 2026 systematic review also noted that premeasurement protocols related to heavy exercise, water intake, and alcohol were inconsistently reported across BIA studies, making it difficult to quantify how much measurement conditions influenced device performance. ([MDPI](https://www.mdpi.com/2411-5142/11/1/65))

That is decisive for downstream use. If the export contains "body_fat_percent" but not the premeasurement context used in validation, including recent food or drink intake, caffeine, alcohol, smoking, heavy exercise, hydration-related restrictions, and device-use conditions, the number is over-labeled.

## Why trend tracking does not qualify

The trend argument is plausible but not proven enough for inclusion.

A trend metric should be included as objective data only if independent evidence shows that the direction of change is reliable under typical-use conditions. The body-composition evidence cited here does not reach that bar. The 2026 systematic review excluded longitudinal body-composition-change studies, and the smartwatch-BIA study against the four-compartment model explicitly stated that future follow-up testing is needed before relying on smartwatch BIA to monitor change over time. ([MDPI](https://www.mdpi.com/2411-5142/11/1/65), [Aquila Digital Community](https://aquila.usm.edu/fac_pubs/20489/))

Consistency may reduce noise for one careful user. By itself, it does not create validation for exported population-scale data.

## Biological age and healthspan scores are not direct measurements

Wearables can directly measure or collect some signals, such as optical pulse waveforms, motion, and sometimes impedance. The product pages and validation papers cited here describe the age and healthspan outputs as estimates, composites, or algorithmic scores rather than direct measurements of "biological age," "healthspan," "pace of aging," or "metabolic age." ([WHOOP](https://www.whoop.com/us/en/thelocker/Healthspan-Data-Meets-Longevity/), [Ultrahuman](https://blog.ultrahuman.com/blog/introducing-ultra-age/), [Oura Support](https://support.ouraring.com/hc/en-us/articles/28451491040019-Cardiovascular-Age), [Samsung Global Newsroom](https://news.samsung.com/global/unlocking-new-possibilities-for-preventative-wellness-with-new-galaxy-watch-and-bioactive-sensor))

WHOOP says Healthspan uses nine metrics across sleep, activity, and fitness, and that WHOOP Age is a proxy for physiological age. That supports the narrower statement that WHOOP chose inputs linked to longevity research; it does not independently validate WHOOP Age as an aging biomarker. ([WHOOP](https://www.whoop.com/us/en/thelocker/Healthspan-Data-Meets-Longevity/))

Ultrahuman says Ultra Age combines sleep, cardiovascular signals, and blood markers into a single trackable insight, with contributors such as Brain Age, Pulse Age, and Blood Age. That is a composite of composites. The broad label is "biological aging"; the supported sensor claim is narrower: some inputs may reflect sleep, cardiovascular waveform features, HRV, or lab biomarkers. ([Ultrahuman](https://blog.ultrahuman.com/blog/introducing-ultra-age/))

Samsung describes AGEs Index as an indicator of metabolic health and biological aging, but its own newsroom footnotes frame Galaxy Watch health features as wellness and fitness tools and say AGEs Index monitoring is not for diagnosis or treatment. ([Samsung Global Newsroom](https://news.samsung.com/global/unlocking-new-possibilities-for-preventative-wellness-with-new-galaxy-watch-and-bioactive-sensor))

## Oura Cardiovascular Age is the strongest case, but still exclude

Among the excluded categories here, vascular age has the clearest mechanistic pathway. Pulse wave velocity is an established measure of arterial stiffness strongly associated with aging, and PPG waveform morphology can contain vascular information. ([UT MD Anderson Cancer Center](https://mdanderson.elsevierpure.com/en/publications/update-on-the-use-of-pulse-wave-velocity-to-measure-age-related-v/), [PLOS Digital Health](https://journals.plos.org/digitalhealth/article?id=10.1371%2Fjournal.pdig.0001329))

Separate PPG-device work also supports that simple PPG-derived pulse-wave-velocity estimates can agree with a referent device, though that does not validate a consumer cardiovascular-age score. ([Frontiers](https://www.frontiersin.org/journals/cardiovascular-medicine/articles/10.3389/fcvm.2023.1108219/full))

A 2026 PLOS Digital Health study tested vascular-age estimation using Oura Ring nocturnal PPG in 160 healthy adults during overnight polysomnography. The model estimated vascular age from pulse waveforms with mean absolute error of 7.25 years for the ring and 6.28 years for a clinical-grade fingertip device, supporting feasibility of wearable PPG vascular-age estimation. ([PLOS Digital Health](https://journals.plos.org/digitalhealth/article?id=10.1371%2Fjournal.pdig.0001329))

But feasibility is not enough for inclusion. The study population was nominally healthy, skewed young, and had very few participants meeting hypertension criteria. The authors noted that larger, more demographically and clinically diverse training data may improve performance and that testing against carotid-femoral PWV and in less healthy participants is needed. ([PLOS Digital Health](https://journals.plos.org/digitalhealth/article?id=10.1371%2Fjournal.pdig.0001329))

The conflict-of-interest note also matters. The Oura waveform data could not be publicly released because of contractual agreements, one author was on Oura's medical advisory board, and two authors later became members of the Oura-National University of Singapore Joint Lab; the authors state that Oura had no role in data analysis, interpretation, or writing. ([PLOS Digital Health](https://journals.plos.org/digitalhealth/article?id=10.1371%2Fjournal.pdig.0001329))

So the narrow finding is: nocturnal ring PPG may contain vascular-age information. The broader consumer feature claim is: a wearable cardiovascular-age number is valid enough for general health interpretation. The narrow finding should not be read as validation of a broad exported metric unless the exported feature, algorithm, population, and intended use match the study's model and validation setting.

## Research aging clocks do not validate product age scores

There is real research interest in wearable-derived aging clocks. A 2025 Nature Communications study developed PpgAge from Apple Watch PPG data in the Apple Heart & Movement Study, using 213,593 participants and more than 149 million participant-days. The model predicted chronological age and found associations between PpgAge gap, cardiometabolic disease, incident events, smoking, exercise, and sleep. ([Nature Communications](https://www.nature.com/articles/s41467-025-64275-4))

That should not be used as validation for WHOOP Age, Ultrahuman Ultra Age, Oura Cardiovascular Age, or Samsung AGEs Index. It supports a specific research model in a specific dataset with its own inputs, training approach, outcomes, limitations, and conflicts.

The PpgAge authors themselves state that behavioral associations are observational and do not establish causal dose-response effects. They also note that the Apple Heart & Movement Study may not be representative, that disease data were self-reported, that additional randomized studies would strengthen the evidence, that conclusions are limited to one study, and that mortality data were unavailable. ([Nature Communications](https://www.nature.com/articles/s41467-025-64275-4))

The conflict-of-interest note is also explicit: several authors were Apple employees and owned Apple stock, and the Apple Heart & Movement Study received funding from Apple and the American Heart Association. ([Nature Communications](https://www.nature.com/articles/s41467-025-64275-4))

## Motivation is not measurement validity

A score may motivate someone to sleep more, walk more, or train consistently. That possible behavioral benefit does not make the score valid as a biological-age measurement.

The evidence bar here is not "could this nudge behavior?" The evidence bar is whether the metric is accurate enough, transparent enough, and validated enough for the specific export label and downstream use. For these age and healthspan scores, the cited evidence does not reach that bar. ([WHOOP](https://www.whoop.com/us/en/thelocker/Healthspan-Data-Meets-Longevity/), [Ultrahuman](https://blog.ultrahuman.com/blog/introducing-ultra-age/), [Oura Support](https://support.ouraring.com/hc/en-us/articles/28451491040019-Cardiovascular-Age), [Samsung Global Newsroom](https://news.samsung.com/global/unlocking-new-possibilities-for-preventative-wellness-with-new-galaxy-watch-and-bioactive-sensor), [Nature Communications](https://www.nature.com/articles/s41467-025-64275-4), [PLOS Digital Health](https://journals.plos.org/digitalhealth/article?id=10.1371%2Fjournal.pdig.0001329))

A motivational feature can stay inside an app as coaching language. It should not become a column named "biological_age," "healthspan," "pace_of_aging," "cardiovascular_age," or "metabolic_age" in a downstream system without validation for that exact interpretation.

## Better alternatives

For body-composition monitoring, simpler measures are often less impressive but more honest. Waist circumference, waist-to-height ratio, body weight trend, strength performance, endurance performance, and standardized progress photos do not directly measure body fat either, but they are more transparent about what they are.

Waist-to-height ratio has evidence as a simple screening marker for cardiometabolic risk, including systematic-review evidence comparing it with BMI and waist circumference. ([PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC3810792/))

The key distinction is labeling. "Waist circumference" is a direct anthropometric measurement. "Body fat percentage from wrist BIA" is a model estimate. "5 km time improved" is a performance outcome. "Biological age decreased by 2 years" is a product-specific interpretation layered on top of uncertain inputs.

## Quick reference

- **Body fat percentage from wrist BIA:** exclude.

- **Fat mass from wrist BIA:** exclude.

- **Lean mass from wrist BIA:** exclude.

- **Skeletal muscle percentage from wrist BIA:** exclude.

- **Body water from wrist BIA:** exclude.

- **Wrist-BIA trend over time:** exclude.

- **WHOOP Age:** exclude.

- **WHOOP Healthspan:** exclude.

- **WHOOP Pace of Aging:** exclude.

- **Ultrahuman Ultra Age:** exclude.

- **Ultrahuman Brain Age:** exclude.

- **Ultrahuman Pulse Age:** exclude.

- **Ultrahuman Blood Age:** exclude.

- **Oura Cardiovascular Age:** exclude as a general-purpose health variable.

- **Samsung AGEs Index:** exclude.


## Practical interpretation

The problem is not that all of these signals are meaningless. Some inputs are real: impedance, PPG waveforms, HRV, sleep duration, activity, blood biomarkers, and pulse-wave morphology can each carry information. ([MDPI](https://www.mdpi.com/2411-5142/11/1/65), [Frontiers](https://www.frontiersin.org/journals/sports-and-active-living/articles/10.3389/fspor.2025.1644082/full), [PLOS Digital Health](https://journals.plos.org/digitalhealth/article?id=10.1371%2Fjournal.pdig.0001329), [Nature Communications](https://www.nature.com/articles/s41467-025-64275-4), [Ultrahuman](https://blog.ultrahuman.com/blog/introducing-ultra-age/))

The problem is label inflation. A signal that may support a narrow statement becomes a marketed age, healthspan, recovery, or metabolic-health score. Then the score is exported without the caveats, measurement conditions, algorithm details, validation cohort, or uncertainty interval.

For human coaching, that may be tolerable. For context-stripped health-data systems, it is not.

## References

- Oliver CJ, Del Vecchio L, Minehan M, Climstein M, Rosic N, Myers S, Tinsley G. [The validity of bioelectrical impedance analysis compared to a four-compartment model in healthy adults: a systematic review](https://www.mdpi.com/2411-5142/11/1/65). _Journal of Functional Morphology and Kinesiology_. 2026;11(1):65. DOI: [10.3390/jfmk11010065](https://doi.org/10.3390/jfmk11010065).

- Carrier B, Melvin AC, Outwin JR, Wasserman MG, Audet AP, Soldes KC, Kozloff KM, Lepley AS. [Wearables for health monitoring: body composition estimates of commercial smartwatch and clinical bioelectrical impedance device](https://www.frontiersin.org/journals/sports-and-active-living/articles/10.3389/fspor.2025.1644082/full). _Frontiers in Sports and Active Living_. 2025;7:1644082. DOI: [10.3389/fspor.2025.1644082](https://doi.org/10.3389/fspor.2025.1644082). Funding note: the study was funded by Samsung Electronics Co. Ltd.; the paper states the sponsor had no role in analysis, interpretation, or submission.

- Brandner CF, Tinsley GM, Graybeal AJ. [Smartwatch-based bioimpedance analysis for body composition estimation: precision and agreement with a four-compartment model](https://aquila.usm.edu/fac_pubs/20489/). _Applied Physiology, Nutrition, and Metabolism_. 2023;48(2):172-182. DOI: [10.1139/apnm-2022-0301](https://doi.org/10.1139/apnm-2022-0301).

- Yilmaz G, Ghorbani S, Ong JL, Golkashani HA, Zhang C, Yeo BTT, et al. [Vascular age estimation using a consumer wearable sleep tracker](https://journals.plos.org/digitalhealth/article?id=10.1371%2Fjournal.pdig.0001329). _PLOS Digital Health_. 2026;5(3):e0001329. DOI: [10.1371/journal.pdig.0001329](https://doi.org/10.1371/journal.pdig.0001329). Conflict note: one author was on Oura's medical advisory board, two authors later joined the Oura-NUS Joint Lab, and Oura waveform data could not be publicly released because of contractual agreements; the authors state Oura had no role in data analysis, interpretation, or writing.

- Marshall AG, Neikirk K, Afolabi J, Mwesigwa N, Shao B, Kirabo A, Reddy AK, Hinton A. [Update on the use of pulse wave velocity to measure age-related vascular changes](https://mdanderson.elsevierpure.com/en/publications/update-on-the-use-of-pulse-wave-velocity-to-measure-age-related-v/). _Current Hypertension Reports_. 2024;26(3):131-140. DOI: [10.1007/s11906-023-01285-x](https://doi.org/10.1007/s11906-023-01285-x).

- Zieff G, Stone K, Paterson C, et al. [Pulse-wave velocity assessments derived from a simple photoplethysmography device: agreement with a referent device](https://www.frontiersin.org/journals/cardiovascular-medicine/articles/10.3389/fcvm.2023.1108219/full). _Frontiers in Cardiovascular Medicine_. 2023;10:1108219. DOI: [10.3389/fcvm.2023.1108219](https://doi.org/10.3389/fcvm.2023.1108219).

- Miller AC, Futoma J, Abbaspourazad S, Heinze-Deml C, Emrani S, Shapiro I, Sapiro G. [A wearable-based aging clock associates with disease and behavior](https://www.nature.com/articles/s41467-025-64275-4). _Nature Communications_. 2025;16:9264. DOI: [10.1038/s41467-025-64275-4](https://doi.org/10.1038/s41467-025-64275-4). Conflict note: multiple authors were Apple employees and owned Apple stock; the Apple Heart & Movement Study received funding from Apple and the American Heart Association.

- Ashwell M, Gunn P, Gibson S. [Waist-to-height ratio is a better screening tool than waist circumference and BMI for adult cardiometabolic risk factors: systematic review and meta-analysis](https://pmc.ncbi.nlm.nih.gov/articles/PMC3810792/). _Obesity Reviews_. 2012;13(3):275-286. DOI: [10.1111/j.1467-789X.2011.00952.x](https://doi.org/10.1111/j.1467-789X.2011.00952.x).

- Oura. [Cardiovascular Age](https://support.ouraring.com/hc/en-us/articles/28451491040019-Cardiovascular-Age). Product documentation, used only to identify marketed feature claims, not as validation evidence.

- WHOOP. [Healthspan White Paper: The Data-Driven Path to Longevity](https://www.whoop.com/us/en/thelocker/Healthspan-Data-Meets-Longevity/). Product documentation, used only to identify marketed feature claims, not as validation evidence.

- Ultrahuman. [Introducing Ultra Age: a new marker for biological aging](https://blog.ultrahuman.com/blog/introducing-ultra-age/). Product documentation, used only to identify marketed feature claims, not as validation evidence.

- Samsung. [Unlocking New Possibilities for Preventative Wellness With New Galaxy Watch and BioActive Sensor](https://news.samsung.com/global/unlocking-new-possibilities-for-preventative-wellness-with-new-galaxy-watch-and-bioactive-sensor). Product documentation and newsroom material, used only to identify marketed feature claims, not as validation evidence.