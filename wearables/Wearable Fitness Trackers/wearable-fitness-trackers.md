# Wearable Fitness Trackers

The most debated questions about what consumer wearables actually measure, what they infer, and where marketing outpaces evidence.

**Status:** Seeking contributors. Each section frames a controversy. Evidence needed.

---

## What Can a Consumer Wearable Physically Measure?

Most consumer wearables measure a narrow set of physical signals: photoplethysmography (PPG) detects pulse and pulse timing from blood-volume changes. Accelerometers detect movement. Single-lead ECG (on devices that have it) records a rhythm strip. Temperature sensors track skin temperature trends. Bioimpedance sensors measure electrical resistance across tissue. CGM sensors (separate adhesive devices, not wrist-worn) measure interstitial glucose.

That's the physical measurement layer. Everything else on the dashboard - recovery scores, readiness scores, stress levels, strain, sleep stages, VO2 max, biological age, cardiovascular age, healthspan, body composition, blood pressure estimates, calorie burn, metabolic fitness - is an inference built on top of those signals. The inference can range from reasonable (estimating heart rate from PPG) to tenuous (estimating biological age from a combination of PPG, temperature, and movement data).

The distinction between measurement and inference is the single most important thing a wearable user can understand, and it's the distinction no brand is incentivized to make clear. The dashboard presents measured and inferred quantities with identical confidence, identical precision, and identical visual weight.

**Competing claims:**

1. The measurement-inference distinction is fundamental and should be communicated clearly to users - when a device displays "recovery: 67%" with the same confidence as "heart rate: 62 bpm," it creates a false equivalence between a direct measurement and a proprietary model output with unknown validity
2. All health measurement involves inference at some level - even a hospital pulse oximeter uses algorithms, and consumer wearables are simply further along the inference chain; the question is whether the inference is validated, not whether it exists
3. Brands deliberately blur the line between measurement and inference because the inferred quantities (recovery, readiness, stress, age) are what differentiate products and justify subscription pricing - the direct measurements alone wouldn't sustain the business model
4. Users don't need to understand the technical pipeline - what matters is whether the output is accurate and actionable, regardless of whether it comes from a direct sensor or a model; the focus should be on validation, not on educating consumers about sensor physics

**Evidence needed:** Consumer comprehension studies on what users believe wearables measure vs what they infer, sensor signal-to-output pipeline documentation by brand, classification frameworks for measurement vs inference in consumer health devices, regulatory perspectives on labeling inferred health outputs.

---

## Is Wearable Heart Rate Accurate Enough to Be Useful?

Heart rate is the most fundamental wearable measurement. PPG-based optical heart rate sensors detect pulse by shining light into the skin and measuring changes in blood volume. Under ideal conditions - rest, good contact, no motion - the signal is clean and accurate. As conditions degrade - intense exercise, poor fit, cold extremities, sweat, ambient light, motion artifact - accuracy degrades with them.

The pattern across validation studies is consistent: resting and nocturnal heart rate from wrist and ring devices is generally reliable. Exercise heart rate becomes less trustworthy as intensity increases, particularly during activities with significant wrist movement (CrossFit, rowing, kettlebell work). The gap between "resting HR is useful" and "exercise HR is reliable" is wider than most users realize.

The skin tone question adds another layer. Multiple studies have found worse PPG accuracy in darker skin during exercise, likely because melanin absorbs more of the green light wavelengths used by most optical sensors. The evidence isn't perfectly consistent across all studies and devices, but the signal is real enough to matter.

**Competing claims:**

1. Resting and nocturnal heart rate from modern wearables is accurate enough to be clinically useful for trend tracking - it can detect changes in fitness, illness, overtraining, and recovery over weeks and months, and represents the most defensible use case for consumer heart rate monitoring
2. Exercise heart rate from wrist-worn devices is unreliable enough to mislead training decisions - heart rate zone training based on inaccurate mid-workout readings can lead to undertrained or overtrained sessions, and chest straps remain necessary for anyone using HR-guided training seriously
3. Accuracy disparities across skin tones are a meaningful equity issue - if devices work worse for darker-skinned users during the activities where accuracy matters most (exercise), the technology is systematically underserving a portion of its user base, and this should be disclosed and addressed
4. The practical accuracy is "good enough" for most consumers - wearable HR doesn't need to match a medical ECG monitor; for the purposes of general fitness tracking, even a ±5-10 bpm error during exercise doesn't fundamentally change behavior for recreational exercisers

**Evidence needed:** Wearable heart rate validation studies stratified by activity type and intensity, skin tone and PPG accuracy meta-analyses, resting vs exercise accuracy comparisons across devices, longitudinal studies on resting HR trends from wearables and health outcomes, chest strap vs wrist vs ring accuracy head-to-head comparisons.

---

## Can Your Watch Screen for Heart Conditions?

Atrial fibrillation detection is the strongest clinical evidence for any consumer wearable feature. Devices with ECG capability (Apple Watch, Samsung Galaxy Watch, WHOOP) can record a single-lead rhythm strip, and the algorithms for identifying AF from these strips have been validated with high sensitivity and specificity in meta-analyses. Irregular rhythm notifications from PPG (without ECG) are a step below but still show reasonable screening performance for AF in multiple studies.

This is genuinely useful. AF is common, often asymptomatic, significantly increases stroke risk, and is treatable with anticoagulation. A wearable that prompts someone to get a clinical evaluation for AF they wouldn't have otherwise discovered has real clinical value.

The problem is how this capability is marketed. "AF screening" becomes "heart health monitoring." A device that can reliably detect one specific arrhythmia is positioned alongside dashboards showing "cardiovascular age," "heart health scores," and vague cardiac wellness metrics that have no comparable validation. The strong evidence for AF detection lends credibility to a much broader set of cardiac claims that haven't earned it.

**Competing claims:**

1. Wearable AF screening is a genuine public health advance - AF is underdiagnosed, the screening performance is strong, and the cost of widespread screening via devices people already wear is essentially zero; this is one case where a consumer device delivers real clinical value
2. AF screening on wearables will generate a large number of false positives in low-risk populations (young, healthy users) - the positive predictive value in a 25-year-old with a low baseline AF prevalence is very different from a 65-year-old, and unnecessary cardiology referrals and anxiety are real costs
3. The strong AF evidence is being used to launder weaker cardiac claims - placing AF screening next to "cardiovascular age" or "heart health score" on the same device implies similar validity, which misleads users about what the device can actually assess beyond rhythm
4. A wearable alert is a screening prompt, not a diagnosis - the clinical pathway should always be wearable alert to clinical ECG to cardiology evaluation, and the risk is that users either over-trust (self-diagnosing and self-treating) or under-trust (ignoring repeated alerts) the device

**Evidence needed:** Wearable AF detection sensitivity and specificity meta-analyses, false-positive rates by age and risk group, clinical pathway studies (wearable alert to diagnosis to treatment), impact of AF screening on stroke incidence, validation data for broader "heart health" features compared to AF-specific features.

---

## Are Recovery, Readiness, and Stress Scores Meaningful?

This may be the single largest gap between marketing and evidence in consumer health technology.

WHOOP Recovery. Garmin Body Battery. Garmin Training Readiness. Oura Readiness Score. Samsung Energy Score. Ultrahuman Dynamic Recovery. FITTR HART recovery and stress outputs. These composite scores take inputs from HRV, sleep data, activity, respiratory rate, temperature, and sometimes other signals, run them through proprietary algorithms, and produce a single number or color that tells you how "recovered" or "ready" or "stressed" you are.

Users make real decisions based on these scores daily. They skip workouts when recovery is "red." They push harder when readiness is "green." They modify training plans, adjust sleep behavior, and calibrate their perceived wellbeing against a number on a screen.

The algorithms are proprietary. The physiological basis for the specific weighting of inputs is not published. The validation against meaningful external criteria is thin. Independent reviewers have found that the validity, physiological meaning, and transparency of these scores remain unclear across manufacturers. The raw inputs (HRV, sleep duration) have some individual value. The composite score that combines them claims to know something about your body's state that the individual inputs don't - and that claim is largely unsubstantiated.

**Competing claims:**

1. Composite scores are the useful layer - raw HRV and sleep data are too noisy and too difficult for consumers to interpret; the score synthesizes multiple signals into an actionable output, and even if the algorithm isn't published, the user experience of a simple green/yellow/red readiness indicator drives better decisions than raw numbers would
2. The scores are proprietary black boxes with no independent validation and no published physiological rationale - users are making training and health decisions based on numbers that may not correlate with actual recovery, readiness, or stress; this is worse than having no score at all because it creates false confidence
3. The commercial incentive is to make scores feel responsive and useful, not to make them accurate - a recovery score that never changes doesn't retain subscribers; a score that fluctuates in ways that feel meaningful keeps users engaged, regardless of whether the fluctuations reflect real physiology
4. Even if the absolute score is meaningless, relative changes within an individual over time may capture something real - if your readiness score consistently drops during periods you know are high-stress and recovers when you rest well, the personal trend may have value even if the underlying algorithm is unvalidated

**Evidence needed:** Independent validation of composite scores against objective recovery markers (performance testing, hormonal markers, immune function), correlation studies between branded scores and self-reported recovery, algorithm transparency and physiological rationale documentation, user decision-making studies (do score-guided decisions produce better outcomes than intuition alone).

---

## HRV From a Wearable: Real Signal or Overinterpreted Noise?

Heart rate variability - the variation in time between successive heartbeats - is a real physiological signal that reflects autonomic nervous system balance. Higher HRV generally indicates greater parasympathetic (rest-and-digest) tone. Lower HRV is associated with stress, fatigue, illness, overtraining, and higher all-cause mortality in epidemiological data. The physiology is legitimate.

The wearable implementation introduces several layers of uncertainty. Nighttime HRV, measured during stable sleep with good device contact, can be reasonably captured by some devices - ring-based measurements in particular tend to perform better than wrist devices for nocturnal HRV because of fewer motion artifacts and better contact. But even a well-measured HRV value is highly variable night to night. A single morning HRV reading is noisy enough that its day-to-day fluctuations may reflect measurement error and normal biological variation more than any meaningful change in autonomic state. The signal becomes useful only when averaged over multiple nights and tracked as a trend.

The problem is what happens after measurement. Brands take the HRV signal and feed it into composite algorithms that produce recovery, readiness, and stress outputs. The distance between "we measured your HRV reasonably well last night" and "your body is 43% stressed" is a distance filled with unvalidated inference.

**Competing claims:**

1. Wearable nighttime HRV, averaged over 5-7 days, provides a genuine signal about autonomic balance and recovery trends - it can identify periods of accumulated stress, illness onset, and adaptation to training, and represents one of the more defensible wearable biomarkers
2. Single-day HRV readings are too noisy to act on - the within-individual day-to-day coefficient of variation is large enough that one low reading means essentially nothing, and users who modify their training based on a single morning HRV are responding to noise
3. The physiological significance of wearable HRV in healthy, non-clinical populations is overstated - most of the strong HRV-health associations come from clinical populations (post-MI, heart failure), and extrapolating to young healthy athletes adjusting their training based on RMSSD changes of a few milliseconds is a stretch
4. Ring-based HRV measurement is meaningfully more reliable than wrist-based measurement for nocturnal readings - device form factor matters, and treating all wearable HRV as equivalent obscures real differences in signal quality

**Evidence needed:** Wearable HRV validation against reference ECG-based HRV, day-to-day coefficient of variation for wearable HRV in healthy populations, optimal averaging windows (how many nights produce a stable trend), ring vs wrist HRV accuracy head-to-head comparisons, wearable HRV-guided training decisions and performance/recovery outcomes.

---

## Can Your Wearable Accurately Track Sleep?

Sleep is one of the most heavily marketed wearable features and one of the most thoroughly studied by independent researchers. The evidence is remarkably consistent across studies and devices.

Wearables are good at detecting that you are asleep. Sleep sensitivity (correctly identifying sleep when you are sleeping) is typically above 90% across modern devices. This makes total sleep time estimates roughly usable - not perfect, but in the right ballpark.

Wearables are bad at detecting that you are quietly awake. Wake specificity (correctly identifying wakefulness when you are awake but lying still) is poor across devices. If you're lying in bed unable to sleep, reading, or just resting quietly, the device will often score you as sleeping. This inflates total sleep time and reduces the accuracy of sleep efficiency calculations.

Sleep staging - the breakdown into light, deep, and REM - is where accuracy degrades most. The gold standard for sleep staging is polysomnography (PSG) with EEG, which measures brain electrical activity. Wearables infer sleep stages from movement, heart rate, and HRV. These are correlates of sleep stages, not direct measurements. Independent polysomnography validation studies consistently show modest staging agreement at best. Company-funded studies tend to report higher accuracy than independent studies.

**Competing claims:**

1. Wearable sleep tracking is useful for the thing most people actually need: knowing approximately how much they slept and whether their sleep patterns are consistent over time - total sleep time and regularity trends are the actionable outputs, and wearables capture these adequately
2. Sleep stage breakdowns (minutes of deep sleep, REM cycles, sleep architecture) are presented with false precision - users wake up, see "32 minutes of deep sleep," and conclude they slept poorly, when the device's ability to distinguish deep from light sleep is not reliable enough to support that conclusion
3. Poor wake detection is a specific problem that biases the data in a specific direction - it makes sleep look better than it is, which may prevent people from recognizing genuine sleep problems; if you spent 45 minutes awake in the middle of the night and your device recorded 8 hours of sleep, the tracking is actively misleading
4. The discrepancy between company-funded and independent validation studies should make consumers skeptical of accuracy claims in marketing materials - when the company's own studies show substantially better performance than independent researchers find, the marketing numbers are likely optimistic

**Evidence needed:** Multi-device polysomnography validation studies by independent researchers, sleep staging accuracy stratified by device and form factor (ring vs wrist), wake detection specificity across devices, comparison of company-funded vs independent accuracy findings, longitudinal studies on whether wearable sleep data leads to improved sleep behavior.

---

## Should You Trust Wearable Calorie Estimates?

Accelerometers count steps reasonably well when gait is regular. Step-count error across devices is generally in the range that's acceptable for habit tracking - knowing you walked roughly 8,000 steps versus 12,000 is useful even if the number is off by several hundred. Steps are one of the most defensible wearable outputs because the measurement is relatively direct (detecting repetitive motion) and the use case is coarse (more vs less activity, not precise quantification).

Energy expenditure is a fundamentally different problem. No wearable can measure how many calories you burn. The device estimates calories by combining movement data, heart rate, and user-entered information (weight, age, sex) in a model. The model makes assumptions about your metabolic rate, your movement efficiency, the thermic effect of food, and your substrate oxidation - none of which it can measure.

Across validation studies, calorie estimates from wearables show large and inconsistent errors. The direction of error varies by device, activity type, and individual. The result: a calorie-burn number that's sometimes 20% too high, sometimes 30% too low, and sometimes close to accurate, with no way for the user to know which situation they're in on any given day.

The downstream consequence matters. People use calorie-burn estimates to calibrate food intake. "I burned 600 calories in that workout, so I can eat 600 more" is a diet decision anchored to a number that may be off by 150-200 calories. Over weeks, this compounds into meaningful surplus or deficit errors.

**Competing claims:**

1. Step counts are useful for behavioral nudging and general activity tracking - the error is small enough relative to the use case that it doesn't undermine the value; knowing your broad activity level day to day helps
2. Calorie-burn estimates from wearables are not accurate enough to guide nutrition decisions - using device-estimated expenditure to set calorie intake or calculate deficits creates a false sense of precision that can derail both fat loss and performance nutrition
3. The calorie number has behavioral value even if it's inaccurate - seeing a higher number motivates more activity, and the relative comparison (harder workout = higher number) provides useful feedback even if the absolute value is wrong
4. Wearable companies should stop displaying calorie-burn numbers with single-digit precision (e.g., "487 calories") when the error bars span hundreds of calories - the display format implies a precision the measurement cannot support

**Evidence needed:** Wearable energy expenditure validation against indirect calorimetry across activity types, error magnitude and direction by device, user behavior studies (do people eat more when told they burned more), step count accuracy across gait patterns and speeds, impact of calorie display precision on user perception.

---

## Is Wearable VO2 Max Worth Tracking?

No wearable directly measures VO2 max. The device estimates it from heart rate, pace, movement, and model assumptions about the user's physiology. The estimate requires the user to be doing a sustained aerobic effort (typically outdoor running or walking) during which heart rate and pace can be tracked simultaneously. The algorithm then maps the relationship between heart rate and workload to an estimated VO2 max using population-based models.

The fundamental limitation: population-based models assume average biomechanics, average cardiac output relationships, and average oxygen extraction. Any individual who deviates from "average" - which is most people - will get a systematically biased estimate. Running economy, cardiac drift, heat, altitude, dehydration, fatigue, and terrain all affect the heart rate-workload relationship without changing actual VO2 max.

Validation studies consistently show systematic overestimation compared to laboratory CPET (cardiopulmonary exercise testing). Some implementations perform better in specific contexts - certain Garmin models in runners doing repeatable outdoor routes, for example. But the errors are large enough that the absolute number is unreliable for most users.

**Competing claims:**

1. Wearable VO2 max is useless as an absolute number but potentially useful as a trend - if the same device, under similar conditions, shows a consistent upward or downward trend over months, that trend likely reflects a real change in fitness even if the absolute value is off
2. The trend argument breaks down because the estimate is sensitive to so many non-fitness variables (heat, fatigue, hydration, terrain, time of day) that week-to-week fluctuations are noise, not signal - you need months of data to see a real trend, and by then you already know whether you're fitter from your training
3. Wearable VO2 max creates a false benchmark that discourages people from getting actually tested - someone sees "VO2 max: 45" on their watch and thinks they know their fitness level, when a lab test might reveal it's 38 or 52; the fake precision displaces real measurement
4. For runners doing consistent outdoor training, wearable VO2 max estimates are reasonable enough to be useful as a training feedback metric - not a clinical measurement, but a data point that responds to training load and fitness changes in a directionally correct way

**Evidence needed:** Wearable VO2 max validation against CPET across devices and populations, systematic bias quantification (overestimation magnitude), test-retest reliability under controlled vs variable conditions, trend accuracy over months vs absolute accuracy at any single point, population subgroup analyses (trained vs untrained, runners vs other activities).

---

## Can a Watch Measure Blood Pressure?

This is where marketing is most aggressively outpacing evidence. True blood pressure measurement requires detecting the force of blood against arterial walls. A cuff does this directly through oscillometry. A wrist-worn optical sensor cannot.

Cuffless blood pressure from PPG works by inference: the algorithm estimates pulse transit time or pulse wave features from the optical signal and maps them to a blood pressure value using models calibrated (often by the user) against a traditional cuff reading. The relationship between pulse wave characteristics and blood pressure is real but noisy, affected by vascular tone, hydration, position, temperature, and individual arterial compliance.

Some devices (WHOOP, Samsung in supported markets) market blood-pressure-related features directly. Apple positions its hypertension notifications as prompts to check with a cuff rather than as direct measurements. The distinction matters clinically: blood pressure numbers guide medication decisions, and inaccurate values could lead to under- or over-treatment.

**Competing claims:**

1. Cuffless wearable blood pressure is not ready for clinical use - systematic reviews find clinically important discrepancies, especially at night and at the extremes (high and low BP) where accuracy matters most; cardiology consensus recommends validated cuff devices until cuffless technology is properly validated
2. Even inaccurate blood pressure tracking could have population-level benefits by prompting people to check their blood pressure who otherwise never would - hypertension is massively underdiagnosed, and a noisy wearable alert that sends someone to a pharmacy cuff is better than no awareness at all
3. Calibration against a cuff creates a false sense of accuracy - the device may read accurately right after calibration and drift over hours and days as vascular conditions change, giving the user confidence in a number that's no longer reliable
4. The technology will improve, and early adoption drives the data collection and iteration needed to get there - dismissing current implementations as useless ignores that this is a rapidly advancing field, and current devices are stepping stones to validated cuffless BP measurement

**Evidence needed:** Cuffless wearable blood pressure validation against ambulatory blood pressure monitoring (ABPM), systematic reviews and meta-analyses of cuffless BP accuracy, calibration drift studies over hours and days, clinical decision impact analyses (would wearable BP numbers change treatment decisions inappropriately), user comprehension studies (do people understand the limitations of cuffless BP).

---

## Wearable Blood Oxygen and Sleep Apnea Screening

Consumer wrist and ring devices estimate blood oxygen saturation (SpO2) using PPG - measuring the ratio of oxygenated to deoxygenated hemoglobin based on how red and infrared light are absorbed. This is the same principle as hospital pulse oximetry, but with worse sensor positioning (wrist or finger vs fingertip), more motion artifact, and less controlled contact pressure.

The result is a measurement that's directionally useful but not clinically precise. Validation studies show mean absolute SpO2 differences that are large enough to matter for clinical decisions. Some specific device validations have failed accuracy testing under both normal and low-oxygen conditions. A reading of 94% might be 92% or 96% in reality - a range that crosses clinical thresholds.

Sleep apnea screening features (Apple, Samsung) use overnight SpO2 patterns and other signals to flag potential sleep-disordered breathing. These are more interesting than static SpO2 numbers because they're looking at patterns (repeated desaturations) rather than absolute values, and pattern detection is more forgiving of absolute accuracy limitations.

**Competing claims:**

1. Consumer wrist/ring SpO2 is not accurate enough for clinical decision-making - it should not be used for oxygen titration, COPD monitoring, or any scenario where precise oxygen saturation matters; the margin of error crosses clinical thresholds
2. SpO2 trends over a night, even if the absolute numbers are imprecise, can flag patterns suggestive of sleep-disordered breathing - repeated desaturation events are a different signal than a single spot-check, and the pattern may be more robust than the individual readings
3. Sleep apnea screening notifications are a valuable public health feature given that the vast majority of moderate-to-severe sleep apnea goes undiagnosed - a wearable prompt that sends someone to get a formal sleep study is worth the false positives
4. These features should be clearly labeled as screening prompts, not as diagnostic tools - the risk is that users either over-interpret a normal reading as ruling out sleep apnea or self-diagnose based on an abnormal notification without seeking clinical confirmation

**Evidence needed:** Consumer SpO2 validation against medical pulse oximetry during sleep, sleep apnea screening notification sensitivity and specificity against polysomnography, false-positive and false-negative rates in real-world use, clinical pathway studies (wearable notification to sleep study to diagnosis), comparison of wearable screening vs questionnaire-based screening (STOP-BANG) for identifying undiagnosed sleep apnea.

---

## Is Overnight Respiratory Rate From a Wearable Useful?

Respiratory rate during sleep is inferred from cyclic variations in the PPG signal, accelerometer data, or both. Unlike SpO2 (which measures an absolute chemical quantity), respiratory rate is a rhythmic signal - the device detects the periodicity of breathing-related motion or pulse modulation, not the depth or quality of each breath.

This makes it technically easier to estimate than SpO2. The cyclic signal is relatively robust during stable sleep when motion artifact is low. As an overnight trend, respiratory rate from wearables is plausible and often serviceable.

The clinical value is in trajectory, not in any single night's reading. A stable overnight respiratory rate that begins trending upward over days or weeks could signal the onset of illness, fluid retention, or worsening cardiopulmonary status. Some clinical research has explored respiratory rate trends for early detection of COVID-19 and other respiratory infections via wearable data.

**Competing claims:**

1. Overnight respiratory rate is one of the more defensible wearable metrics because the measurement conditions are favorable (minimal motion during sleep) and the clinical signal is established - respiratory rate is a vital sign used in hospital early warning scores, and longitudinal tracking from home could provide early illness detection
2. The clinical utility for healthy users is low - respiratory rate is stable night after night in well people, and the deviations that would matter clinically (infection, heart failure decompensation) are rare events that would likely be detected through symptoms before a respiratory rate trend catches them
3. Respiratory rate is more useful than SpO2 from a wearable because it relies on pattern detection rather than absolute chemical measurement - the device doesn't need to know the exact breaths-per-minute to detect a meaningful change from the user's own baseline
4. The metric is being buried under flashier features - no brand prominently markets respiratory rate because it's not exciting, yet it may be among the most technically sound and clinically grounded outputs a wearable produces

**Evidence needed:** Wearable respiratory rate validation against reference methods during sleep, longitudinal respiratory rate trends and illness detection (sensitivity and lead time), clinical utility in healthy vs chronically ill populations, comparison of respiratory rate trend detection across device types.

---

## Skin Temperature and Symptom Dashboards: Signal or Decoration?

Skin temperature sensors on wearables (Apple Watch, Oura, WHOOP, Ultrahuman) detect changes in peripheral skin temperature relative to the user's own baseline. This is a real, measurable physical quantity. Peripheral skin temperature does shift with circadian rhythm, menstrual cycle phase, illness onset, and changes in ambient conditions. The sensor can capture a trend.

What happens next is where measurement becomes interpretation. Brands build features on top of temperature data: "Symptom Radar" (Oura), "Health Monitor" (WHOOP), hormonal "insights" (multiple brands), and illness-onset notifications. These features combine temperature deviations with other signals (HRV, respiratory rate, sleep) and produce dashboards that suggest the device is monitoring your immune status, hormonal state, or overall health trajectory.

Peripheral skin temperature is not core body temperature. It's affected by ambient conditions, clothing, blanket use, room temperature, alcohol, vasoconstriction, and physical contact with a partner. The signal is real but context-dependent and indirect.

**Competing claims:**

1. Baseline temperature deviation tracked over weeks is genuinely informative - it can detect menstrual cycle phase shifts, illness onset, and recovery patterns; the signal is physiologically grounded even if it's noisy and indirect
2. "Symptom dashboards" and "health monitor" features that layer interpretation on top of temperature and other signals overstate what the device can detect - a temperature rise could mean you're getting sick, or that you slept under a heavier blanket, or that ambient temperature changed; the algorithm can't distinguish these
3. Temperature's greatest value may be in menstrual cycle phase estimation, where the biphasic temperature pattern (lower in follicular phase, higher in luteal phase) is well-established physiology - this is a more grounded use case than vague "symptom" detection
4. The branded dashboards (Symptom Radar, Health Monitor) create an illusion of medical monitoring that isn't warranted - users may develop false confidence that their device would alert them to illness, when in reality the feature's sensitivity and specificity for detecting clinically relevant events is unvalidated

**Evidence needed:** Wearable skin temperature accuracy against reference sensors, sensitivity and specificity of temperature-based illness detection features, temperature trend and menstrual cycle phase correlation studies, user comprehension and behavioral response to symptom notifications, ambient and behavioral confounders on wrist/finger temperature measurement.

---

## Can Your Ring Predict Ovulation?

Menstrual cycle tracking through wearables uses skin temperature trends, resting heart rate, HRV, and sometimes respiratory rate to estimate cycle phase. The underlying physiology is sound: progesterone rises after ovulation, increasing core and peripheral temperature by roughly 0.2-0.5°C. This biphasic pattern is the basis of the temperature method of fertility awareness, which predates wearables by decades.

The distinction that matters: detecting that ovulation has already occurred (retrospective phase estimation from the temperature shift) is much easier than predicting when ovulation will occur in the current cycle. Retrospective confirmation within a few days is moderately achievable. Prospective prediction of the exact fertile window for conception or avoidance is harder and less reliable, especially in people with irregular cycles.

The evidence quality issue is acute in this category. Multiple published wearable ovulation studies were funded by the device companies and authored by company employees, some with financial interests in the company's stock. Independent systematic reviews find more modest accuracy than company-published results suggest. Accuracy degrades further in irregular cycles, which are exactly the cycles where prediction would be most valuable.

**Competing claims:**

1. Wearable cycle phase estimation is moderately useful for understanding your body's patterns - knowing approximately where you are in your cycle, retrospectively, has value for training periodization, symptom tracking, and general awareness, even if the exact day isn't pinpointed
2. Claiming to predict the fertile window or ovulation day accurately enough for family planning - either for conception or avoidance - is a higher bar than current wearable evidence supports; the consequences of being wrong (unplanned pregnancy or missed conception window) make this a high-stakes use case that demands higher validation standards
3. Company-funded and company-authored validation studies should not be the basis for marketing ovulation accuracy claims - independent validation with pre-registered protocols and no conflicts of interest is the minimum standard for a feature with reproductive health implications
4. Wearables may actually be useful for subfertile couples trying to conceive, where identifying an approximate fertile window is better than no information - the stakes of a false negative (missed window) are different from the stakes of relying on the device for contraception

**Evidence needed:** Independent wearable ovulation detection validation against urinary LH and ultrasound-confirmed ovulation, accuracy in irregular vs regular cycles, prospective vs retrospective detection accuracy, conflict-of-interest analysis of published wearable fertility studies, user comprehension of what "ovulation detected" means on their device.

---

## Wearable Glucose Tracking and Metabolic Scores

This category splits cleanly in two based on whether the product uses an actual sensor or just an algorithm.

If the product includes a CGM sensor (a small adhesive device on the arm that measures interstitial glucose via an electrochemical reaction), it is measuring a real biological quantity. The glucose trace is real data. Meal responses, fasting patterns, overnight trends, and the glycemic impact of different foods are directly observable. This applies to products like Ultrahuman M1 and integrations where Oura or other devices display data from an external CGM.

The second layer is what brands build on top of that data: "metabolic fitness scores," "meal scores," "metabolic health grades," "glucose zone summaries." These take the raw glucose signal - which is genuine - and run it through proprietary scoring algorithms to produce a branded output. The glucose curve after a meal is real. The "meal score of 7.2" is an interpretation with unclear validation and no standardized meaning.

For devices that don't use a CGM but still market "metabolic health" features derived from HRV, temperature, activity, and other non-glucose signals, the inference chain is even longer and less grounded.

**Competing claims:**

1. Raw CGM data is genuinely useful for people who want to understand their glycemic responses - seeing how your body handles different foods, exercise timing, and sleep is actionable information, and wearable-integrated CGMs make this accessible outside clinical settings
2. Proprietary metabolic scores layered on CGM data add a marketing interpretation to a signal that users could interpret themselves - the raw glucose curve is more informative than a single score, and the scoring algorithm may emphasize or de-emphasize aspects of the response based on the brand's model rather than the user's actual health context
3. CGM-based wearable products are being marketed to healthy, non-diabetic populations where the clinical value of continuous glucose monitoring is debated - the device measures a real signal, but whether that signal is actionable for metabolically healthy people is a separate question from whether it's accurate
4. "Metabolic health" features that don't include an actual glucose sensor - inferring metabolic status from HRV, temperature, and activity alone - are a further step removed from direct measurement and should not be equated with CGM-based products

**Evidence needed:** CGM accuracy validation in consumer wearable integrations vs standalone medical CGMs, proprietary metabolic score validation against established metabolic health markers (HOMA-IR, OGTT, HbA1c), behavioral outcomes from CGM use in non-diabetic populations, comparison of raw glucose data interpretation vs branded scoring for user decision-making.

---

## Body Composition, Biological Age, and Healthspan Scores

Body composition from a wrist-worn device uses bioelectrical impedance analysis (BIA) - sending a small electrical current through the body and measuring resistance to estimate fat mass, lean mass, and water content. The problem is that BIA is highly sensitive to hydration status, contact quality, body position, skin moisture, and the modeling assumptions used to convert impedance to composition. Even medical-grade BIA devices with multiple electrodes and controlled conditions have significant individual-level error. Wrist-based BIA, with a single contact point and no control over user conditions, magnifies every source of error.

Systematic reviews of consumer BIA devices against reference methods (DXA, multi-compartment models) find limits of agreement too wide to detect the small changes in body composition that users are trying to track. A week-to-week change of 0.5% body fat is well within the noise of the measurement. Yet the device displays it as a concrete number.

Beyond body composition, several brands market age-related composite scores: WHOOP Age, WHOOP Healthspan, Ultrahuman Ultra Age, Oura Cardiovascular Age, Samsung AGEs index. None of these quantities are directly measured by the device. They are model outputs derived from proxies of proxies - HRV, sleep, temperature, activity, and sometimes SpO2 combined into a proprietary algorithm that outputs an "age" or "healthspan" number.

**Competing claims:**

1. Wrist-based body composition is not accurate enough for individual tracking - the measurement error exceeds the changes most users are trying to detect, and the resulting numbers create false narratives about progress or regression that aren't grounded in real body composition changes
2. Trend tracking may have some value if users are consistent about measurement conditions (same time, same hydration) - even if absolute values are wrong, directional changes over months might reflect real trends, though the noise-to-signal ratio remains poor
3. Biological age, healthspan, and cardiovascular age scores from wearables are the most marketing-heavy, least evidence-backed category of consumer health outputs - they combine already-uncertain inputs through unvalidated algorithms to produce a number that implies clinical meaning without clinical validation
4. These features serve a motivational purpose even if the numbers aren't precise - seeing a "biological age" improve or "healthspan" increase may reinforce healthy behavior, and the behavioral nudge has value independent of measurement accuracy

**Evidence needed:** Consumer wrist BIA validation against DXA and multi-compartment models, limits of agreement for individual-level tracking, age-score algorithm transparency and validation against established aging biomarkers, user behavior studies on whether age/healthspan scores motivate sustained lifestyle change, comparison of wearable body composition to simpler alternatives (waist circumference, progress photos, performance metrics).

---

## Only 11% of Wearables Have Been Validated - Should That Worry You?

A living umbrella review of systematic reviews on wearable accuracy found that only about 11% of commercial devices had been validated for at least one health outcome in peer-reviewed literature. The other 89% market health features based on internal testing, proprietary benchmarks, or no publicly available evidence at all.

Some features go through formal regulatory clearance. ECG and AF detection features on Apple Watch, Samsung, and WHOOP have gone through FDA 510(k) or CE marking processes that require clinical validation. Sleep apnea notifications have their own clearance pathway. These regulatory submissions require the company to demonstrate safety and efficacy with clinical data.

Most wearable features don't go through regulatory clearance because they're positioned as "wellness" rather than "medical" features. Recovery scores, stress scores, sleep stages, VO2 max estimates, body composition, age scores, readiness outputs, and calorie estimates are marketed under the wellness umbrella, which has no validation requirement. The features look medical. The dashboards feel clinical. But the regulatory pathway treats them as lifestyle products.

**Competing claims:**

1. The 89% validation gap is a serious consumer protection issue - devices are making health-adjacent claims that influence behavior and health decisions without evidence that those claims are accurate; "wellness" positioning shouldn't exempt features from basic accuracy validation
2. Requiring validation for every feature would stifle innovation and increase costs, ultimately slowing the development of technology that could eventually become clinically useful - the current regulatory approach allows rapid iteration that peer-reviewed validation can't match
3. The burden should be on consumers and clinicians to understand the limitations rather than on regulators to certify every feature - health literacy about wearables is the scalable solution, not regulatory expansion
4. A tiered approach is needed: features that influence clinical decisions (blood pressure, SpO2, ECG, sleep apnea) should require regulatory validation; features positioned as behavioral nudges (steps, activity tracking) can be lighter; features that claim to measure recovery, readiness, or biological age should be somewhere in between, with at minimum transparent methodology and published validation

**Evidence needed:** Updated validation coverage surveys across consumer wearable brands and features, regulatory framework comparisons across jurisdictions (FDA, CE, other), user perception studies (do people treat wellness features as medical information), health outcome studies comparing validated vs unvalidated feature use, transparency audits of proprietary algorithm documentation.

---

## Do Company-Funded Studies Inflate Wearable Accuracy?

The pattern in wearable validation research is consistent enough to be notable. Studies conducted by independent researchers, with no financial ties to device manufacturers, tend to report lower accuracy than studies funded by or involving employees of the device companies. This has been observed across brands and across feature categories.

In sleep tracking, independent polysomnography validations show modest staging accuracy, while company-affiliated studies report substantially higher agreement. In ovulation prediction, company-funded papers authored by employees with stock ownership report strong accuracy, while independent systematic reviews find more moderate performance. The same device, measuring the same quantity, appears more accurate when the company evaluates itself than when external researchers do.

This doesn't necessarily mean fraud. Company-run studies often use optimal conditions (selected participants, controlled environments, latest firmware, post-hoc algorithm tuning) that independent researchers can't or don't replicate. The device may genuinely perform better in ideal conditions. But users don't wear their devices in ideal conditions. They wear them in bed with a partner, during sweaty workouts, on wrists of varying circumference, in rooms of varying temperature. The real-world accuracy is what matters, and that's what independent studies are more likely to capture.

**Competing claims:**

1. The accuracy gap between company and independent studies is a systemic problem that undermines the evidence base for wearable health claims - marketing materials cherry-pick the best-performing studies, which are disproportionately company-funded, and this inflates user expectations
2. Company-funded studies aren't automatically biased - they often have larger sample sizes, better device access, and more controlled protocols; the issue is transparency about funding, conflicts of interest, and whether the study conditions reflect real-world use
3. Independent validation should be the minimum standard before marketing health accuracy claims - if a feature hasn't been validated by researchers with no financial stake in the result, accuracy claims should not appear in consumer-facing materials
4. The solution is pre-registration and data sharing rather than dismissing all company research - requiring companies to pre-register validation studies and make raw data available would reduce selective reporting while still allowing manufacturer expertise in study design

**Evidence needed:** Systematic comparisons of accuracy findings in company-funded vs independently funded wearable studies, funding source analysis of published wearable validation literature, impact of study conditions (lab vs free-living) on reported accuracy, proposals for validation standards and transparency requirements.

---

## Do Wearables Actually Improve Health Behavior?

The implicit premise of the wearable industry: tracking health data leads to better health decisions, which leads to better health outcomes. The question is whether this premise holds.

Step counting has the most behavioral evidence. Multiple studies show that people who track steps walk more, and that step goals increase daily activity. This is real and useful. It may be the strongest behavioral case for any wearable feature.

Beyond steps, the evidence thins. Do sleep scores lead to better sleep? Or do they create performance anxiety about sleep (orthosomnia - the clinical term for anxiety about achieving perfect sleep metrics) that paradoxically worsens sleep? Do recovery scores improve training periodization? Or do they create dependence on an external number that replaces body awareness? Do glucose overlays change long-term dietary patterns? Or do they create short-term reactivity to individual meals that doesn't translate to sustained behavioral change?

The "quantified self" movement assumes that more data is better. But there's a plausible counter-case: constant health quantification creates a medicalized relationship with your own body, where normal physiological variation becomes a source of anxiety, and health becomes a dashboard to optimize rather than a state to inhabit.

**Competing claims:**

1. Wearables improve health behavior through awareness and feedback loops - seeing concrete data about activity, sleep, and recovery creates accountability and motivation that drives meaningful behavior change, especially for people who are just beginning to engage with their health
2. The behavioral benefits are concentrated in simple metrics (steps, activity reminders, sleep regularity) and don't extend to complex composite scores - showing someone their step count motivates walking; showing someone a recovery score of 47% doesn't produce a clear behavioral response because the action it implies is ambiguous
3. Wearables may worsen health behavior in some users by creating data dependency, anxiety, and orthorexic tendencies - people who can't exercise without checking their readiness score, can't eat without logging their glucose response, or can't sleep without worrying about their sleep score may have a less healthy relationship with their body than people with no device at all
4. The behavioral impact is highly individual - some people thrive with data, others are harmed by it; the question isn't whether wearables help or hurt but whether each user is in the group that benefits, and currently there's no way to predict which group someone will fall into before they start tracking

**Evidence needed:** RCTs on wearable use and health outcomes (step count, physical activity, sleep quality, weight management), orthosomnia prevalence studies, recovery/readiness score-guided vs intuition-guided training outcome comparisons, long-term behavioral sustainability of wearable-driven health changes (do habits persist after the novelty wears off), psychological impact assessments of continuous health quantification.

---

## How to Contribute

Pick a section. Find the relevant meta-analyses, systematic reviews, or high-quality RCTs. Summarize what the evidence shows, including limitations.

See [CONTRIBUTING.md](../../CONTRIBUTING.md) for citation standards.
