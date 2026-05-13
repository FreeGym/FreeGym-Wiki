# Is Wearable Heart Rate Accurate Enough to Be Useful?

Heart rate is not one wearable metric. A nocturnal average from a validated ring, a resting value from a still wrist, a mid-workout wrist reading, and a chest-strap exercise trace are different measurements. Exporting all of them as `heart_rate` collapses the conditions that determine whether the number is valid. ([Wang et al., 2017](https://jamanetwork.com/journals/jamacardiology/fullarticle/2566167); [Cao et al., 2022](https://www.jmir.org/2022/1/e27487/); [Schweizer and Gilgen-Ammann, 2025](https://cardio.jmir.org/2025/1/e67110/); [Hung et al., 2025](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0318724))

## Bottom line

**Resting and nocturnal wearable heart rate should be included when the exported metric preserves the resting/nocturnal context.** This is the most defensible consumer wearable heart-rate use case. ([Lambe et al., 2026](https://www.nature.com/articles/s41746-025-02238-1); [Cao et al., 2022](https://www.jmir.org/2022/1/e27487/); [Fiore et al., 2024](https://www.mdpi.com/2076-3417/14/23/10778); [Feng et al., 2024](https://www.jmir.org/2024/1/e60493/))

**Generic wearable heart rate should be excluded.** A context-free `heart_rate` column mixes reliable low-motion readings with less reliable exercise and high-motion readings. ([Wang et al., 2017](https://jamanetwork.com/journals/jamacardiology/fullarticle/2566167); [Nelson and Allen, 2019](https://mhealth.jmir.org/2019/3/e10828/); [Schweizer and Gilgen-Ammann, 2025](https://cardio.jmir.org/2025/1/e67110/))

**Wrist-worn and ring-based exercise heart rate should be excluded for AI-exported metrics.** Some wrist devices perform well in some structured exercise settings, but device model, movement pattern, skin contact, wearing position, exercise intensity, and skin tone can materially change accuracy. Those caveats do not survive export. Ring HR validation is strongest for nocturnal HR, not exercise HR. ([Wang et al., 2017](https://jamanetwork.com/journals/jamacardiology/fullarticle/2566167); [Pasadyn et al., 2019](https://cdt.amegroups.org/article/view/26754/html); [Cao et al., 2022](https://www.jmir.org/2022/1/e27487/); [Fiore et al., 2024](https://www.mdpi.com/2076-3417/14/23/10778); [Hung et al., 2025](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0318724))

**Chest-strap ECG heart rate and independently validated upper-arm optical heart rate can be included when the source and wearing position are preserved.** In head-to-head validation, chest straps consistently outperform wrist devices during exercise, and one recent arm-worn optical validation found excellent agreement when worn on the upper arm. ([Wang et al., 2017](https://jamanetwork.com/journals/jamacardiology/fullarticle/2566167); [Pasadyn et al., 2019](https://cdt.amegroups.org/article/view/26754/html); [Schweizer and Gilgen-Ammann, 2025](https://cardio.jmir.org/2025/1/e67110/))

## Metric verdicts for exported data

|Exported metric|Verdict|Reason|
|---|--:|---|
|`resting_heart_rate_trend`|**Include**|Low-motion/resting HR has independent validation and is most useful as a longitudinal trend. ([Lambe et al., 2026](https://www.nature.com/articles/s41746-025-02238-1); [Feng et al., 2024](https://www.jmir.org/2024/1/e60493/); [Nelson and Allen, 2019](https://mhealth.jmir.org/2019/3/e10828/))|
|`nocturnal_mean_heart_rate_trend`|**Include**|Sleep-period HR from rings/watches has strong agreement with ECG in validation studies, especially as nightly averages. ([Cao et al., 2022](https://www.jmir.org/2022/1/e27487/); [Fiore et al., 2024](https://www.mdpi.com/2076-3417/14/23/10778))|
|`resting_heart_rate_absolute`|**Include**|Include only when the metric name preserves resting context; do not merge it into generic HR. ([Lambe et al., 2026](https://www.nature.com/articles/s41746-025-02238-1); [Feng et al., 2024](https://www.jmir.org/2024/1/e60493/))|
|`nocturnal_mean_heart_rate_absolute`|**Include**|Include only when the metric name preserves nocturnal averaging. ([Cao et al., 2022](https://www.jmir.org/2022/1/e27487/); [Fiore et al., 2024](https://www.mdpi.com/2076-3417/14/23/10778))|
|`exercise_heart_rate_chest_strap`|**Include**|Chest-strap ECG-style monitors are the most validated exercise option in head-to-head studies. ([Wang et al., 2017](https://jamanetwork.com/journals/jamacardiology/fullarticle/2566167); [Pasadyn et al., 2019](https://cdt.amegroups.org/article/view/26754/html))|
|`exercise_heart_rate_validated_upper_arm_optical`|**Include**|Include only for independently validated upper-arm optical sensors with source retained. ([Schweizer and Gilgen-Ammann, 2025](https://cardio.jmir.org/2025/1/e67110/))|
|`heart_rate`|**Exclude**|Too broad. It hides rest, sleep, exercise, device, source, motion, and wearing-position context. ([Wang et al., 2017](https://jamanetwork.com/journals/jamacardiology/fullarticle/2566167); [Nelson and Allen, 2019](https://mhealth.jmir.org/2019/3/e10828/); [Schweizer and Gilgen-Ammann, 2025](https://cardio.jmir.org/2025/1/e67110/))|
|`exercise_heart_rate_wrist`|**Exclude**|Wrist accuracy varies materially during exercise and can produce errors large enough to mislead training zones. ([Wang et al., 2017](https://jamanetwork.com/journals/jamacardiology/fullarticle/2566167); [Pasadyn et al., 2019](https://cdt.amegroups.org/article/view/26754/html); [Hung et al., 2025](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0318724))|
|`exercise_heart_rate_ring`|**Exclude**|Ring HR validation cited here is nocturnal rather than exercise validation. ([Cao et al., 2022](https://www.jmir.org/2022/1/e27487/); [Fiore et al., 2024](https://www.mdpi.com/2076-3417/14/23/10778))|
|`heart_rate_zone_minutes_wrist`|**Exclude**|Zone assignment is a derived output from mid-workout wrist HR, whose error during exercise can be large. ([Wang et al., 2017](https://jamanetwork.com/journals/jamacardiology/fullarticle/2566167); [Pasadyn et al., 2019](https://cdt.amegroups.org/article/view/26754/html))|
|`training_load_from_wrist_hr`|**Exclude**|A derived metric built on unreliable exercise HR should not be treated as ground truth. ([Wang et al., 2017](https://jamanetwork.com/journals/jamacardiology/fullarticle/2566167); [Pasadyn et al., 2019](https://cdt.amegroups.org/article/view/26754/html))|
|`recovery_score`, `readiness_score`, or proprietary “heart health” composite|**Exclude**|Proprietary composites obscure inputs, formulas, and validation conditions. ([Doherty et al., 2025](https://www.degruyterbrill.com/document/doi/10.1515/teb-2025-0001/html))|

## What PPG is measuring

Most wrist and ring devices use photoplethysmography (PPG): light is emitted into the skin and reflected or absorbed light is used to estimate pulsatile blood-volume changes. Wrist-based HR monitors then convert that optical signal into heart rate using device-specific processing algorithms. ([Hung et al., 2025](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0318724); [Schweizer and Gilgen-Ammann, 2025](https://cardio.jmir.org/2025/1/e67110/))

That mechanism is plausible for heart rate, but plausibility is not enough. PPG signal quality can be affected by motion, device fit, skin deformation, sensor design, blood flow, vascular changes, sweat, contact pressure, and proprietary post-processing. Nelson and Allen also note that manufacturers use proprietary algorithms and that firmware updates can change the measurement pipeline, which means validation can become stale as devices change. ([Hung et al., 2025](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0318724); [Nelson and Allen, 2019](https://mhealth.jmir.org/2019/3/e10828/))

The measurement gap is this: **PPG supports “pulse-derived heart rate under validated conditions.” It does not support a context-free claim that every exported wearable HR value is accurate.** That is an export-level inference from studies showing strong rest/sleep agreement but material device, motion, exercise-intensity, wearing-position, and skin-tone limits. ([Cao et al., 2022](https://www.jmir.org/2022/1/e27487/); [Wang et al., 2017](https://jamanetwork.com/journals/jamacardiology/fullarticle/2566167); [Schweizer and Gilgen-Ammann, 2025](https://cardio.jmir.org/2025/1/e67110/); [Hung et al., 2025](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0318724))

## Why resting and nocturnal HR earns an include

Low-motion heart rate is the strongest use case. In an overnight home validation study, the Oura Ring was compared with a medical-grade chest ECG in 35 healthy adults. Average-per-night HR had a Pearson correlation of 0.99968 and a mean bias of -0.44 bpm versus ECG. The authors limited the conclusion to nocturnal HR/HRV and noted that awake activity and artifacts need separate validation. Oura Health provided access to the data; the authors declared no conflicts of interest. ([Cao et al., 2022](https://www.jmir.org/2022/1/e27487/))

A smart-ring meta-analysis found that, across three Oura nocturnal HR studies using ECG comparators, pooled nocturnal HR bias was -0.41 bpm with limits of agreement from -2.65 to 1.81 bpm. The same review found that cardiovascular smart-ring studies used ECG in five studies, but four cardiovascular studies had private funding, so ring evidence should be read with attention to funding. The meta-analysis itself reported no external funding and no conflicts of interest. ([Fiore et al., 2024](https://www.mdpi.com/2076-3417/14/23/10778))

A 2026 living systematic review and meta-analysis of Apple Watch measurements included 82 studies and found a small pooled HR bias of -0.27 bpm, with limits of agreement from -7.19 to 6.64 bpm. The authors reported Science Foundation Ireland funding with no funder role and declared no competing interests. This supports Apple Watch HR as one of the better-validated consumer metrics, but the limits of agreement still matter for single readings and high-stakes interpretation. ([Lambe et al., 2026](https://www.nature.com/articles/s41746-025-02238-1))

A larger observational validation in the Project Baseline Health Study compared Verily Study Watch resting HR with ECG in 875 participants and found excellent reliability, with ICC = 0.946 and overall bias of 0.76 bpm. This study also found that wearable RHR tracked expected clinical and fitness-related patterns, including higher BMI, inflammatory markers, diabetes, disability score, lower six-minute walk distance, and lower step count. This trial was funded by Verily Life Sciences; Verily was responsible for data collection, and several authors reported Verily employment and equity. The findings are useful, but the manufacturer-linked conflict should be kept in view. ([Feng et al., 2024](https://www.jmir.org/2024/1/e60493/))

The practical conclusion is narrow: **include resting/nocturnal HR as a trend and, when clearly labeled, as an absolute value. Do not generalize that validation to exercise HR or proprietary recovery labels.** ([Lambe et al., 2026](https://www.nature.com/articles/s41746-025-02238-1); [Cao et al., 2022](https://www.jmir.org/2022/1/e27487/); [Fiore et al., 2024](https://www.mdpi.com/2076-3417/14/23/10778); [Doherty et al., 2025](https://www.degruyterbrill.com/document/doi/10.1515/teb-2025-0001/html))

## Why exercise HR from the wrist earns an exclude

Exercise is where wrist PPG becomes unstable. In a JAMA Cardiology validation study, wrist devices showed variable agreement with ECG during treadmill testing. The Polar H7 chest strap had the highest agreement with ECG, while wrist devices had lower agreement; Apple Watch and Mio Fuse had 95% limits of agreement from -27 to +29 bpm, Fitbit Charge HR from -34 to +39 bpm, and Basis Peak from -39 to +33 bpm. The authors concluded that wrist monitors were best at rest, diminished with exercise, and that electrode-containing chest monitors should be used when accurate HR is imperative. The study reported no conflicts and non-industry foundation support. ([Wang et al., 2017](https://jamanetwork.com/journals/jamacardiology/fullarticle/2566167))

In a prospective athlete study, the Polar H7 chest strap again had the greatest agreement with ECG, followed by Apple Watch III, with other wrist devices lower. The authors reported that accuracy fell off at high intensity and concluded that, when accuracy is imperative, a chest strap or Apple Watch III may be the best choice. The authors declared no conflicts of interest. For an app user on a treadmill, that may be helpful. For an AI-exported `exercise_heart_rate_wrist` metric, it is not enough: the validation is device-specific, activity-specific, and population-specific. ([Pasadyn et al., 2019](https://cdt.amegroups.org/article/view/26754/html))

A 24-hour ecologically valid intraindividual study comparing Apple Watch 3 and Fitbit Charge 2 with ambulatory ECG found low overall error and low sleep error, but larger errors during activities of daily living and some wide single-reading deviations. The authors concluded that aggregated accuracy was acceptable in most conditions, but any single real-time observation could have a large error. They also noted erratic wrist movement as a likely driver of error and declared no conflicts of interest. ([Nelson and Allen, 2019](https://mhealth.jmir.org/2019/3/e10828/))

A 2025 validation comparing Polar devices found a clear wearing-position effect. The Polar Verity Sense worn on the upper arm showed minimal bias, MAPE 1.35%, and excellent agreement with ECG chest strap; the wrist-worn Polar Vantage V2 showed only moderate accuracy and increased variability. The authors declared no conflicts of interest. This supports **validated upper-arm optical HR** as an include, but it does not rescue generic wrist HR. ([Schweizer and Gilgen-Ammann, 2025](https://cardio.jmir.org/2025/1/e67110/))

The training implication is direct: **heart-rate zone minutes derived from wrist exercise HR should be excluded.** A device that is sometimes off by tens of bpm can move a user across zones, and the derived zone or training-load metric inherits that uncertainty. ([Wang et al., 2017](https://jamanetwork.com/journals/jamacardiology/fullarticle/2566167); [Pasadyn et al., 2019](https://cdt.amegroups.org/article/view/26754/html))

## Skin tone is an equity and validation issue

Skin tone evidence is mixed, but it is not ignorable. A systematic review summarized in later work found ten studies on skin tone and optical HR accuracy: four found no differences across skin tones, four found lower accuracy with darker skin, and two found mixed results. This means the evidence base is inconsistent, not reassuring. ([Mulholland et al., 2025](https://link.springer.com/article/10.1007/s00421-025-05977-x); [Hung et al., 2025](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0318724))

A 2025 PLOS One study compared Fitbit Charge 5 with a Polar H10 chest strap across Fitzpatrick skin-tone groups during rest and graded cycling exercise. Resting error was similar across groups, but exercise error increased with intensity in medium and darker skin-tone groups. At >60% heart-rate reserve, the dark skin-tone group had mean error of 16.5 bpm versus 3.5 bpm in the light skin-tone group. The study was publicly/academically funded, funders had no role, and the authors declared no competing interests. ([Hung et al., 2025](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0318724))

A 2025 European Journal of Applied Physiology study used objective skin-pigmentation measurement rather than only categorical skin tone. It found strong overall HR agreement for Apple Watch Series 8, Garmin vivosmart 5, and SlateSafety BAND V2 during cycling, with average MAE under 5 bpm across intensities. Skin pigmentation increased HR error only slightly for the SlateSafety device, but darker pigmentation negatively affected data quality across tested devices. The authors declared no competing interests. ([Mulholland et al., 2025](https://link.springer.com/article/10.1007/s00421-025-05977-x))

The verdict is not “all devices fail darker skin.” The verdict is: **generic wrist-exercise HR should be excluded because the validation base does not prove reliable performance across the populations likely to rely on it, and some recent evidence shows errors that are materially larger in darker-skinned users during exercise.** Resting/nocturnal HR remains included because the skin-tone signal at rest is less concerning in the available evidence, but exports should still preserve device and context. ([Hung et al., 2025](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0318724); [Mulholland et al., 2025](https://link.springer.com/article/10.1007/s00421-025-05977-x))

## Illness, recovery, and “heart health” claims

Wearable HR trends can contribute to illness-detection models, but the claim must stay narrow. A Lancet Digital Health systematic review of wearable sensors for SARS-CoV-2 detection found algorithm performance varied widely, with AUCs from 0.52 to 0.92 and presymptomatic detection ranging from 20% to 88% of cases; increased heart rate was one of the most frequently associated signals. The authors concluded the evidence was promising but early and called for larger prospective, controlled, diverse studies. ([Mitratza et al., 2022](https://www.sciencedirect.com/science/article/pii/S258975002200019X))

That supports **trend anomaly detection** as a research direction. It does not support exporting `heart_health`, `illness_risk`, `recovery`, or `readiness` as ground-truth metrics unless the specific composite has independent validation, documented inputs, and preserved acquisition context. A 2025 review of composite health scores found that none of the reviewed manufacturers disclosed exact algorithmic formulas and that few provided empirical validation or peer-reviewed evidence supporting score accuracy or clinical relevance. ([Mitratza et al., 2022](https://www.sciencedirect.com/science/article/pii/S258975002200019X); [Doherty et al., 2025](https://www.degruyterbrill.com/document/doi/10.1515/teb-2025-0001/html))

The brand-inflation gap is important: **the sensor supports “heart rate under validated conditions,” not broad “heart health.”** A validated resting HR trend is not the same as cardiovascular diagnosis, recovery status, overtraining status, stress resilience, or readiness to train. ([Lambe et al., 2026](https://www.nature.com/articles/s41746-025-02238-1); [Doherty et al., 2025](https://www.degruyterbrill.com/document/doi/10.1515/teb-2025-0001/html))

## Quick reference values

- Apple Watch systematic review/meta-analysis: 82 studies; HR mean bias -0.27 bpm; limits of agreement -7.19 to 6.64 bpm. ([Lambe et al., 2026](https://www.nature.com/articles/s41746-025-02238-1))

- Oura nocturnal HR validation: average-per-night HR correlation 0.99968; mean bias -0.44 bpm versus ECG. ([Cao et al., 2022](https://www.jmir.org/2022/1/e27487/))

- Smart-ring meta-analysis: pooled Oura nocturnal HR bias -0.41 bpm; limits of agreement -2.65 to 1.81 bpm. ([Fiore et al., 2024](https://www.mdpi.com/2076-3417/14/23/10778))

- Verily Study Watch RHR validation: 875 participants; ICC 0.946 versus ECG; bias 0.76 bpm. Manufacturer-funded; several authors had Verily employment/equity. ([Feng et al., 2024](https://www.jmir.org/2024/1/e60493/))

- JAMA wrist exercise validation: chest strap agreement with ECG 0.99; wrist-device limits of agreement as wide as roughly +/-30 to +/-40 bpm depending on device. ([Wang et al., 2017](https://jamanetwork.com/journals/jamacardiology/fullarticle/2566167))

- 2025 Fitbit skin-tone exercise study: dark skin-tone group mean error 16.5 bpm at >60% HR reserve versus 3.5 bpm in light skin-tone group. ([Hung et al., 2025](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0318724))

- 2025 objective-pigmentation study: Apple/Garmin/SlateSafety average MAE under 5 bpm across intensities, but darker pigmentation negatively affected data quality. ([Mulholland et al., 2025](https://link.springer.com/article/10.1007/s00421-025-05977-x))


## Practical interpretation

- **Include resting/nocturnal HR trend.** This is the cleanest wearable HR metric and the one least likely to pollute downstream models when named correctly. ([Lambe et al., 2026](https://www.nature.com/articles/s41746-025-02238-1); [Cao et al., 2022](https://www.jmir.org/2022/1/e27487/); [Fiore et al., 2024](https://www.mdpi.com/2076-3417/14/23/10778))

- **Include absolute resting/nocturnal HR only when the context is encoded in the metric name.** `resting_heart_rate` is acceptable; `heart_rate` is not. ([Lambe et al., 2026](https://www.nature.com/articles/s41746-025-02238-1); [Cao et al., 2022](https://www.jmir.org/2022/1/e27487/); [Feng et al., 2024](https://www.jmir.org/2024/1/e60493/))

- **Exclude wrist and ring exercise HR.** A human can sometimes interpret it cautiously; an AI pipeline cannot recover missing context. ([Wang et al., 2017](https://jamanetwork.com/journals/jamacardiology/fullarticle/2566167); [Pasadyn et al., 2019](https://cdt.amegroups.org/article/view/26754/html); [Cao et al., 2022](https://www.jmir.org/2022/1/e27487/))

- **Include chest-strap or validated upper-arm exercise HR only when the source is preserved.** `exercise_hr_chest_strap` and `exercise_hr_upper_arm_optical_validated` are different metrics from `exercise_hr_wrist`. ([Wang et al., 2017](https://jamanetwork.com/journals/jamacardiology/fullarticle/2566167); [Pasadyn et al., 2019](https://cdt.amegroups.org/article/view/26754/html); [Schweizer and Gilgen-Ammann, 2025](https://cardio.jmir.org/2025/1/e67110/))

- **Exclude proprietary recovery/readiness/heart-health composites.** They inflate a narrow validated signal into a broader health claim that the sensor evidence does not support. ([Doherty et al., 2025](https://www.degruyterbrill.com/document/doi/10.1515/teb-2025-0001/html); [Lambe et al., 2026](https://www.nature.com/articles/s41746-025-02238-1))


## References

- [Lambe R, Baldwin M, O’Grady B, et al. The accuracy of Apple Watch measurements: a living systematic review and meta-analysis. _npj Digital Medicine_. 2026;9:63. DOI: 10.1038/s41746-025-02238-1.](https://www.nature.com/articles/s41746-025-02238-1) No competing interests declared; supported by Science Foundation Ireland with no funder role.

- [Cao R, Azimi I, Sarhaddi F, et al. Accuracy assessment of Oura Ring nocturnal heart rate and heart rate variability in comparison with electrocardiography. _Journal of Medical Internet Research_. 2022;24:e27487. DOI: 10.2196/27487.](https://www.jmir.org/2022/1/e27487/) Oura Health provided access to data; NSF support; no conflicts declared.

- [Fiore M, Bianconi A, Sicari G, Conni A, Lenzi J, Tomaiuolo G, Zito F, Golinelli D, Sanmarchi F. The use of smart rings in health monitoring - a meta-analysis. _Applied Sciences_. 2024;14(23):10778. DOI: 10.3390/app142310778.](https://www.mdpi.com/2076-3417/14/23/10778) No external funding; no conflicts declared. Included cardiovascular smart-ring studies had mixed funding, including private funding.

- [Feng KY, Short SA, Shah SH, et al. Resting heart rate and associations with clinical measures from the Project Baseline Health Study. _Journal of Medical Internet Research_. 2024;26:e60493. DOI: 10.2196/60493.](https://www.jmir.org/2024/1/e60493/) Funded by Verily Life Sciences; several authors reported Verily employment and equity.

- [Wang R, Blackburn G, Desai M, et al. Accuracy of wrist-worn heart rate monitors. _JAMA Cardiology_. 2017;2(1):104-106. DOI: 10.1001/jamacardio.2016.3340.](https://jamanetwork.com/journals/jamacardiology/fullarticle/2566167) No author conflicts reported; supported by The Mary Elizabeth Holdsworth Fund at Cleveland Clinic.

- [Pasadyn SR, Soudan M, Gillinov M, et al. Accuracy of commercially available heart rate monitors in athletes: a prospective study. _Cardiovascular Diagnosis and Therapy_. 2019;9(4):379-385. DOI: 10.21037/cdt.2019.06.05.](https://cdt.amegroups.org/article/view/26754/html) No conflicts declared.

- [Nelson BW, Allen NB. Accuracy of consumer wearable heart rate measurement during an ecologically valid 24-hour period. _JMIR mHealth and uHealth_. 2019;7(3):e10828. DOI: 10.2196/10828.](https://mhealth.jmir.org/2019/3/e10828/) No conflicts declared.

- [Schweizer T, Gilgen-Ammann R. Wrist-worn and arm-worn wearables for monitoring heart rate during sedentary and light-to-vigorous physical activities. _JMIR Cardio_. 2025;9:e67110. DOI: 10.2196/67110.](https://cardio.jmir.org/2025/1/e67110/) No conflicts declared.

- [Hung SH, Serwa K, Rosenthal G, Eng JJ. Validity of heart rate measurements in wrist-based monitors across skin tones during exercise. _PLOS One_. 2025;20(2):e0318724. DOI: 10.1371/journal.pone.0318724.](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0318724) Academic/public funding; no competing interests declared.

- [Mulholland AM, MacDonald HV, Aguiar EJ, Wingo JE, et al. Influence of skin pigmentation on the accuracy and data quality of photoplethysmographic heart rate measurement during exercise. _European Journal of Applied Physiology_. 2025. DOI: 10.1007/s00421-025-05977-x.](https://link.springer.com/article/10.1007/s00421-025-05977-x) No competing interests declared.

- [Mitratza M, Goodale BM, Shagadatova A, et al. The performance of wearable sensors in the detection of SARS-CoV-2 infection: a systematic review. _The Lancet Digital Health_. 2022;4(5):e370-e383. DOI: 10.1016/S2589-7500(22)00019-X.](https://www.sciencedirect.com/science/article/pii/S258975002200019X)

- [Doherty C, Baldwin M, Lambe R, Burke D, Altini M. Readiness, recovery, and strain: an evaluation of composite health scores in consumer wearables. _Translational Exercise Biomedicine_. 2025;2(2):128-144. DOI: 10.1515/teb-2025-0001.](https://www.degruyterbrill.com/document/doi/10.1515/teb-2025-0001/html)