# Do Company-Funded Studies Inflate Wearable Accuracy?

Company-funded wearable studies should not be treated as invalid by default. They should be treated as lower-trust evidence for consumer-facing accuracy claims unless independently replicated under realistic conditions.

The best-supported conclusion is narrower than "all company studies are wrong" but stronger than "funding does not matter." Across biomedical drug and medical-device research, industry-sponsored studies are more likely to report favorable efficacy results and favorable conclusions than non-industry-sponsored studies. ([PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC8132492/)) In wearable validation specifically, the literature shows limited validation coverage, documented manufacturer involvement or missing disclosure, incomplete reporting of software and algorithms, proprietary composite metrics, and examples where devices perform differently across controlled, clinical, and free-living evaluations. ([Springer Nature](https://link.springer.com/article/10.1007/s40279-024-02077-2)) ([Springer Nature](https://link.springer.com/article/10.1186/s12966-023-01473-7)) ([Oxford Academic](https://academic.oup.com/sleepadvances/article/6/2/zpaf021/8090472)) ([Nature](https://www.nature.com/articles/s41598-025-93774-z)) ([Sage Journals](https://journals.sagepub.com/doi/10.1177/20552076221084461))

## What the claim is and is not

The claim is not that company-funded wearable studies are fraudulent. Company-funded or company-authored studies can still contribute useful evidence, especially when funding, conflicts of interest, software processing, device versions, algorithms, and cut-points are reported clearly. ([Springer Nature](https://link.springer.com/article/10.1186/s12966-023-01473-7))

The claim is that company involvement changes how accuracy evidence should be interpreted. In the general medical drug/device literature, a Cochrane review of 75 empirical papers found that industry-sponsored studies more often had favorable efficacy results than non-industry-sponsored studies, with RR 1.27, and more often had favorable conclusions, with RR 1.34. The authors concluded that manufacturing-company sponsorship leads to more favorable results and conclusions than other sponsorship sources. ([PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC8132492/))

For wearables specifically, the direct evidence is thinner than the general biomedical evidence. The wearable reviews cited here document validation gaps and reporting limitations, rather than one universal cross-device "industry inflation factor" for wearable accuracy. But the warning signs are substantial enough that company-funded or company-authored studies should not be the sole basis for health accuracy claims. ([Springer Nature](https://link.springer.com/article/10.1007/s40279-024-02077-2)) ([Springer Nature](https://link.springer.com/article/10.1186/s12966-023-01473-7))

## The wearable evidence base is not mature enough for broad trust

A 2024 umbrella review of consumer wearable validation research found 24 systematic reviews covering 249 non-duplicate validation studies and 430,465 participants. Only about 11 percent of commercially available devices had been validated for at least one biomarker, and the authors estimated that the existing validation literature covered only 3.5 percent of the device-biomarker evaluations that would be needed for full coverage. ([Springer Nature](https://link.springer.com/article/10.1007/s40279-024-02077-2))

The same umbrella review found that accuracy varies by metric. Heart rate measures were generally close on average, while energy expenditure, physical activity intensity, VO₂ max, and sleep measures showed larger errors or systematic over/underestimation. The authors also emphasized that algorithms, user characteristics, skin tone, body size, device placement, wear time, and environmental conditions can affect validity. ([Springer Nature](https://link.springer.com/article/10.1007/s40279-024-02077-2))

A systematic review of 545 laboratory validation studies of wearable physical-behavior measures found that 9.5 percent of studies involved the manufacturer through funding, loaned devices, or author relationships; 15.8 percent did not report either funding or conflicts of interest. Software processing was reported in 42.4 percent of studies, and algorithm or cut-point information in 25.1 percent. That limits readers' ability to evaluate how closely each validation result applies to a given software version, algorithm, preprocessing pipeline, or use setting. ([Springer Nature](https://link.springer.com/article/10.1186/s12966-023-01473-7))

## Sleep tracking shows the problem clearly

Sleep is one of the clearest examples of accuracy inflation risk. Consumer devices often detect "sleep" better than they detect wakefulness or sleep stages. In a 2025 polysomnography validation of six consumer wearables, sleep sensitivity exceeded 90 percent, but specificity for wake detection ranged only from 29.39 to 52.15 percent, and sleep-stage agreement was fair to moderate, with Cohen's kappa values from 0.21 to 0.53. The authors noted that proprietary algorithms limit transparency and that independent validation remains limited. ([Oxford Academic](https://academic.oup.com/sleepadvances/article/6/2/zpaf021/8090472))

An independent 2024 study comparing five commercial sleep trackers with polysomnography in young adults found proportional bias across devices: devices tended to overestimate wake after sleep onset on nights with shorter wake time and underestimate it on nights with longer wake time. The same paper noted that proprietary sensors and algorithms make it difficult to access granular data, reproduce methods, or understand why a device performed well or poorly. ([MDPI](https://www.mdpi.com/1424-8220/24/2/635))

The gap becomes larger in clinical populations. A 2025 sleep-lab study of ring trackers in patients found all-stage sleep-classification accuracy of 53.18 percent for Oura, 50.48 percent for SleepOn, and 35.06 percent for Circul when compared with polysomnography. The authors noted that two prior Oura studies declaring conflicts of interest with Oura reported higher accuracy, and that those studies used selected young or healthy participants and excluded sleep disorders. ([Nature](https://www.nature.com/articles/s41598-025-93774-z))

That does not prove fraud. It does show why company-linked, healthy-cohort, ideal-condition studies cannot be generalized to "sleep health" claims for ordinary users, especially users in sleep-clinic or sleep-disorder contexts, or users with fragmented sleep. ([Nature](https://www.nature.com/articles/s41598-025-93774-z))

## Fertility and ovulation prediction show endpoint inflation

Fertility prediction illustrates a different problem: the reported accuracy depends heavily on what counts as success. A company-linked Ava study reported that a machine-learning algorithm detected the fertile window with 90 percent accuracy. That study had a clear financial conflict of interest: several authors were current or former Ava AG employees, and another served on Ava AG's medical advisory board. ([JMIR](https://www.jmir.org/2019/4/e13404/))

An independent exploratory validation of the Ava bracelet under free-living conditions did not validate ovulation prediction directly, but it did test some of the physiological inputs used by the device. In 33 reproductive-aged women, Ava's heart-rate estimates were not comparable to criterion measures from a Polar chest strap. Ava's sleep measures showed some agreement with ActiGraph measures, but the authors concluded that Ava's sleep and heart-rate estimates were not equivalent to criterion measures overall and cautioned against relying on Ava for precise measurement. The authors reported no potential conflicts of interest and university funding. ([Sage Journals](https://journals.sagepub.com/doi/10.1177/20552076221084461))

A 2026 systematic review and Bayesian network meta-analysis of wearable digital technologies for fertility-window and menstrual-cycle detection found pooled accuracy of 0.88, sensitivity of 0.79, and specificity of 0.80. But exact ovulation-day detection was much weaker: pooled accuracy was 0.56 for the exact ovulation day and 0.61 within +/-1 day, improving to about 0.90 only when the window widened to +/-2 days. ([Nature](https://www.nature.com/articles/s41746-025-02320-8))

The inflation gap is therefore not just "company vs independent." It is also "broad window vs exact day." A device can look accurate when the endpoint is detecting a multi-day fertile window and much less accurate when the endpoint is identifying ovulation precisely. A consumer-facing "ovulation tracking" claim can be more precise than the evidence if the validation endpoint is a wider fertile window rather than exact ovulation-day detection. ([Nature](https://www.nature.com/articles/s41746-025-02320-8))

## How accuracy inflation happens without fraud

Accuracy can be inflated by study design. A study may test healthier or more homogeneous participants, use controlled placement and wear conditions, rely on ideal wear time, or choose an endpoint that is easier to hit. Those choices can produce genuinely better results under study conditions while still overstating typical-use accuracy. ([Springer Nature](https://link.springer.com/article/10.1007/s40279-024-02077-2))

Accuracy can also be inflated by metric choice. For sleep, high sleep sensitivity can look impressive because most nighttime epochs are sleep, but the clinically important failure may be poor wake detection or poor sleep-stage classification. For fertility, a wide fertile-window endpoint can look strong while exact ovulation-day detection remains modest. ([Oxford Academic](https://academic.oup.com/sleepadvances/article/6/2/zpaf021/8090472)) ([Nature](https://www.nature.com/articles/s41746-025-02320-8))

Accuracy can be inflated by opacity. If the exported column says "recovery," "readiness," "stress," or "sleep score," but the inputs and weighting are proprietary, the metric is not an independently auditable physiological measurement. The 2024 umbrella review specifically noted that proprietary composite metrics such as "stress," "training readiness," "body battery," and similar bespoke outputs remain insufficiently validated. ([Springer Nature](https://link.springer.com/article/10.1007/s40279-024-02077-2))

## Verdict on the competing claims

The claim that company-funded studies can inflate user expectations is best stated as a cautionary interpretation, not as a directly measured wearable-specific pooled estimate. General drug/device research shows industry sponsorship is associated with more favorable results and conclusions, while wearable research shows incomplete validation, documented manufacturer involvement or missing disclosures, and case examples where independent clinical or free-living studies report lower or more variable accuracy than company-linked or ideal-condition studies. ([PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC8132492/)) ([Springer Nature](https://link.springer.com/article/10.1007/s40279-024-02077-2)) ([Springer Nature](https://link.springer.com/article/10.1186/s12966-023-01473-7)) ([Nature](https://www.nature.com/articles/s41598-025-93774-z)) ([Sage Journals](https://journals.sagepub.com/doi/10.1177/20552076221084461))

The claim that company-funded studies are not automatically biased is also correct. Manufacturer-linked studies can still contribute useful validation data, especially when methods, funding, conflicts of interest, software versions, and algorithms are reported clearly. But that does not make them sufficient for consumer health claims, because tightly controlled protocols often do not represent real-world wear. ([Springer Nature](https://link.springer.com/article/10.1186/s12966-023-01473-7)) ([Springer Nature](https://link.springer.com/article/10.1007/s40279-024-02077-2))

Given the current validation gaps, independent validation is the safest minimum standard. A wearable feature should not be marketed as health-accurate unless researchers with no financial stake have validated the metric in realistic conditions and in the populations likely to rely on it. ([Springer Nature](https://link.springer.com/article/10.1007/s40279-024-02077-2))

Pre-registration, data sharing, firmware or algorithm-version reporting, and independent replication are complementary safeguards. The existing validation literature shows that software processing and algorithm or cut-point details are often underreported, which makes method transparency and version reporting especially important. ([Springer Nature](https://link.springer.com/article/10.1186/s12966-023-01473-7))

## Practical interpretation

- Company-funded wearable validation should be flagged explicitly, not discarded automatically. ([PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC8132492/)) ([Springer Nature](https://link.springer.com/article/10.1186/s12966-023-01473-7))

- Company-funded or company-authored studies should not be treated as sufficient by themselves for consumer-facing health accuracy claims, especially when independent realistic-use validation is absent. ([PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC8132492/)) ([Springer Nature](https://link.springer.com/article/10.1007/s40279-024-02077-2))

- Independent validation under typical-use conditions should be required before a wearable metric is treated as reliable ground-truth data. ([Springer Nature](https://link.springer.com/article/10.1007/s40279-024-02077-2))

- Broad labels such as "sleep health," "recovery," "readiness," "stress," and "ovulation tracking" should be treated as broader than the evidence unless the exact exported metric has independent validation for that exact use. ([Springer Nature](https://link.springer.com/article/10.1007/s40279-024-02077-2)) ([Nature](https://www.nature.com/articles/s41746-025-02320-8))

- If a device is validated only in healthy, young, compliant participants, the claim should not be exported to clinical, older, darker-skin, sleep-disorder, or fragmented-sleep populations without separate validation. ([Springer Nature](https://link.springer.com/article/10.1007/s40279-024-02077-2)) ([Nature](https://www.nature.com/articles/s41598-025-93774-z))


## Bottom line

Company-funded wearable studies can contribute useful evidence, but they should be treated as preliminary, lower-weight evidence for health accuracy claims. The minimum standard should be independent validation, realistic wear conditions, transparent funding and conflicts, algorithm-version reporting, and access to enough raw or epoch-level data for external audit. Without that, health-relevant exported metrics should be treated as unvalidated or excluded from analyses and claims that require ground-truth accuracy. ([Springer Nature](https://link.springer.com/article/10.1007/s40279-024-02077-2)) ([Springer Nature](https://link.springer.com/article/10.1186/s12966-023-01473-7))

## References

- Lundh A, Lexchin J, Mintzes B, Schroll JB, Bero L. [Industry sponsorship and research outcome](https://pmc.ncbi.nlm.nih.gov/articles/PMC8132492/). Cochrane Database of Systematic Reviews. 2017;2:MR000033. DOI: 10.1002/14651858.MR000033.pub3.

- Doherty C, Baldwin M, Keogh A, Caulfield B, Argent R. [Keeping Pace with Wearables: A Living Umbrella Review of Systematic Reviews Evaluating the Accuracy of Consumer Wearable Technologies in Health Measurement](https://link.springer.com/article/10.1007/s40279-024-02077-2). Sports Medicine. 2024. DOI: 10.1007/s40279-024-02077-2.

- Giurgiu M, et al. [Assessment of 24-hour physical behaviour in adults via wearables: a systematic review of validation studies](https://link.springer.com/article/10.1186/s12966-023-01473-7). International Journal of Behavioral Nutrition and Physical Activity. 2023. DOI: 10.1186/s12966-023-01473-7.

- Schyvens AM, Peters B, Van Oost NC, Aerts JM, et al. [A performance validation of six commercial wrist-worn wearable sleep-tracking devices for sleep stage scoring compared to polysomnography](https://academic.oup.com/sleepadvances/article/6/2/zpaf021/8090472). Sleep Advances. 2025;6(2):zpaf021. DOI: 10.1093/sleepadvances/zpaf021.

- Herberger S, et al. [Performance of wearable finger ring trackers for diagnostic sleep measurement in the clinical context](https://www.nature.com/articles/s41598-025-93774-z). Scientific Reports. 2025;15:9461. DOI: 10.1038/s41598-025-93774-z.

- Kainec KA, et al. [Evaluating Accuracy in Five Commercial Sleep-Tracking Devices Compared to Research-Grade Actigraphy and Polysomnography](https://www.mdpi.com/1424-8220/24/2/635). Sensors. 2024;24(2):635. DOI: 10.3390/s24020635.

- Goodale BM, Shilaih M, Falco L, Dammeier F, Hamvas G, Leeners B. [Wearable Sensors Reveal Menses-Driven Changes in Physiology and Enable Prediction of the Fertile Window: Observational Study](https://www.jmir.org/2019/4/e13404/). Journal of Medical Internet Research. 2019;21(4):e13404. DOI: 10.2196/13404.

- Nulty AK, Chen E, Thompson AL. [The Ava bracelet for collection of fertility and pregnancy data in free-living conditions: An exploratory validity and acceptability study](https://journals.sagepub.com/doi/10.1177/20552076221084461). Digital Health. 2022;8:20552076221084461. DOI: 10.1177/20552076221084461.

- Shi Y, Wang CC, Yang Y, et al. [The diagnostic accuracy of wearable digital technology in detecting fertility window and menstrual cycles: a systematic review and Bayesian network meta-analysis](https://www.nature.com/articles/s41746-025-02320-8). npj Digital Medicine. 2026;9:139. DOI: 10.1038/s41746-025-02320-8.