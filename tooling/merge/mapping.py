# Canonical feature mapping for the six-app comparison.
# Hand-written judgement data; build.py turns it into the published outputs.
#
# Token grammar per app string:
#   "12"   claim 12 is a core member of this feature
#   "a12"  claim 12 is an aspect (setting/variant) of this feature: shown, not scored on its own,
#          but it does show the parent capability exists
#   "x12"  claim 12 is primarily mapped elsewhere, but its quote also evidences this feature
# SPLYT has two claim files. data/claims/splyt.json indices are used as-is (0..246);
# the feature index (data/claims/splyt-index.json, published 2026-10-09) is written "i<n>" and
# stored as 247+n in the combined SPLYT list.
#
# App keys: s=splyt h=hevy t=strong g=gravl f=fitbod m=motra

CATEGORIES = {
    "LOG": "Workout logging",
    "SET": "Sets, supersets & loading",
    "PLAN": "Templates, plans & calendar",
    "PROG": "Automatic programming",
    "AI": "AI & voice",
    "LIB": "Exercise library & content",
    "STAT": "Stats & progress",
    "HEALTH": "Health, body & recovery",
    "CARDIO": "Cardio, sports & other activities",
    "WATCH": "Apple Watch & wearables",
    "SOC": "Social & competition",
    "DATA": "Sharing, import/export & integrations",
    "PLAT": "Platforms, widgets & system",
    "PERS": "Personalisation, account & support",
}

FEATURES = []


def F(id, name, cat, definition, s="", h="", t="", g="", f="", m=""):
    FEATURES.append(dict(id=id, name=name, cat=cat, definition=definition,
                         tok=dict(splyt=s, hevy=h, strong=t, gravl=g, fitbod=f, motra=m)))


# ---------------------------------------------------------------- LOG
F("set-logging", "Strength set logging", "LOG",
  "Log weight and reps for each set of a lift during a live workout.",
  s="0 a2 a27 i24 ai3 ai31", h="0 a80", t="x12 x85", g="58", f="57 a66", m="33 x47 a46")
F("empty-workout", "Start an empty workout", "LOG",
  "Start an unplanned workout and add exercises as you go.",
  s="x4 i63", h="1", t="100", g="74", f="51", m="34")
F("previous-performance", "Previous performance shown or pre-filled", "LOG",
  "While logging, each set shows or pre-fills what you lifted last time on that exercise.",
  s="4 a22 a23 i32 i33 ai8", h="23 24 a25 a26", g="x58", m="47 48")
F("live-workout-stats", "Live comparison during a workout", "LOG",
  "During a workout, running totals or a live comparison against previous sessions are shown.",
  s="37 a39 i59", h="45", t="107 a108")
F("rpe-rir", "Effort per set (RPE / RIR)", "LOG",
  "Record perceived exertion or reps in reserve for a set or exercise.",
  s="15 i27", h="27 a28", t="85", g="3", f="62 a63", m="39")
F("workout-effort-rating", "Whole-workout effort rating", "LOG",
  "Rate how hard an entire session felt.",
  s="16 i16", m="40")
F("tempo-tracking", "Lifting tempo tracking", "LOG",
  "Record the tempo of a set.",
  m="x41")
F("quick-complete", "Complete planned sets without entering each", "LOG",
  "Mark a planned workout, group or all remaining sets as done as prescribed instead of entering every set.",
  s="28 a29 i50 ai49", f="45", m="61")
F("workout-notes", "Workout name and notes", "LOG",
  "Give a workout a name and attach a free-text note or description.",
  s="26 a31", h="33", t="32", m="63")
F("workout-media", "Photos or video on a workout", "LOG",
  "Attach photos or video to a logged workout.",
  h="171", t="x33", m="x63")
F("edit-live-workout", "Add and reorder exercises mid-workout", "LOG",
  "Add exercises to, or drag to reorder exercises within, a workout in progress.",
  s="24 i40", h="22", t="101", g="72 73", f="55")
F("exercise-swap", "Exercise swap with suggested alternatives", "LOG",
  "Replace an exercise mid-workout, with the app suggesting suitable alternatives.",
  s="20 i37 ai38", h="94 a95 x22", g="42", f="56", m="56 a57")
F("exercise-notes", "Exercise notes", "LOG",
  "Attach a note to an exercise, kept with the session or shown next time.",
  s="21 i36", h="30 a31 a32", t="34 a35", g="82", f="64", m="x24")
F("grip-tracking", "Grip and attachment tracking", "LOG",
  "Record the grip, handle or attachment used, with history kept per grip.",
  s="18 a19 i34 ai233", m="x4 x5")
F("bodyweight-exercises", "Bodyweight, weighted and assisted exercises", "LOG",
  "Exercises that use body weight, including added load or assistance, are logged and counted correctly.",
  s="30", h="10 11 12 a13", t="10", f="68", m="49")
F("timed-exercises", "Timed exercises", "LOG",
  "Log time-based exercises (e.g. planks) by duration, with a timer.",
  s="i35", h="8 a57 a58", t="11", g="76", f="70", m="52 a51")
F("pause-discard", "Pause, resume or discard a workout", "LOG",
  "Pause the workout clock and resume later, or throw away a workout in progress.",
  s="x124 i47", h="36 37", g="71", f="60 61")
F("edit-past-workouts", "Edit or delete past workouts", "LOG",
  "Change or delete a workout after it has been saved.",
  s="32 i18 ai19", h="40 41 a38", t="94", g="80 81", f="58 59", m="62")
F("log-past-workout", "Log a workout after the fact", "LOG",
  "Record a workout you did earlier, on its real date and time.",
  s="33 i0 ai1", h="39 a44", t="93", g="79", f="54")
F("history-search", "Search workout history", "LOG",
  "Search or filter the list of past workouts.",
  s="181 i20")
F("inactivity-reminder", "Forgotten-workout reminder", "LOG",
  "Prompts you when a workout appears abandoned (inactivity or leaving the location).",
  s="43 i61 ai268", m="59 60")
F("offline-logging", "Offline logging", "LOG",
  "Workouts can be logged and saved without a connection and sync later.",
  s="34 i2", h="196", f="77", m="27 a28")
F("kg-lb", "Kilograms and pounds", "LOG",
  "Choose kilograms or pounds as the weight unit.",
  s="36 i4", h="66", t="30", g="102", f="75", m="54 a55")
F("per-exercise-units", "Per-exercise weight units", "LOG",
  "Use a different weight unit for an individual exercise or piece of equipment.",
  h="67", t="31", g="103", f="76", m="53")
F("keep-screen-awake", "Keep screen awake during workouts", "LOG",
  "Option to stop the phone locking during a workout.",
  s="i60", h="59", m="58")

# ---------------------------------------------------------------- SET
F("rest-timer", "Rest timer", "SET",
  "A countdown (or count-up) between sets, typically starting when a set is completed.",
  s="44 a47 a50 i42 ai45", h="50 a52 a53", t="9 a86 a87 a88", g="59", f="71", m="42")
F("custom-rest", "Custom rest per exercise or set", "SET",
  "Set different rest durations per exercise or per set, remembered next time.",
  s="45 46 a51 i43 i44", h="51", t="89 a90", g="60", f="72", m="44")
F("rest-alerts", "Rest-end alerts", "SET",
  "A sound, vibration, voice cue or notification when rest is over.",
  s="48 i46", h="56 a54 a55", t="a91 92", g="61 x121", f="73", m="43 a45")
F("warmup-sets", "Warm-up set tagging", "SET",
  "Mark sets as warm-ups (kept separate from working sets).",
  s="10 xi28", h="15 a64", t="12", g="x65", f="x37", m="35")
F("warmup-calculator", "Automatic warm-up sets", "SET",
  "The app inserts warm-up sets with calculated weights before working sets.",
  h="63", t="26 a27", g="65", f="37")
F("drop-sets", "Drop sets", "SET",
  "Log a set as a drop set with reduced-weight follow-on efforts.",
  s="8 a9 i29", h="16 a18", t="14", g="64", m="36")
F("failure-sets", "Failure sets", "SET",
  "Mark a set as taken to failure.",
  s="11 i28", h="17", t="13")
F("other-set-types", "Additional set types (top set, partials, cool-down)", "SET",
  "Set-type tags beyond warm-up, drop and failure, such as top sets, partial reps or cool-down sets.",
  s="12 13 i30", m="x35")
F("supersets", "Supersets", "SET",
  "Group two exercises to be performed back-to-back.",
  s="5 i39", h="19 a21", t="15 a17", g="62", f="43 a44", m="37")
F("giant-sets-circuits", "Giant sets and circuits", "SET",
  "Group three or more exercises together as a giant set or circuit.",
  s="6 xi39", h="20", t="16", g="63", f="x43", m="38")
F("set-targets", "Per-set rep targets and pyramids", "SET",
  "Templates can hold rep ranges or different targets per set (pyramids, reverse pyramids).",
  s="14", h="7", g="32 33 a31")
F("plate-calculator", "Plate calculator", "SET",
  "Shows which plates to load for a target weight.",
  s="17 i26 ai25", h="60 a61 a62", t="28 a29", g="68 a69 a70", f="74 a67")

# ---------------------------------------------------------------- PLAN
F("templates", "Saved workout templates", "PLAN",
  "Save reusable workouts and start a session from one.",
  s="75 a40 a78 i136", h="2 a4", t="3 a49", g="77", f="52", m="73 a71 a76 a82")
F("template-organisation", "Template folders or tags", "PLAN",
  "Organise templates into folders or tags.",
  s="76 i139", h="3", t="97 a98", m="75")
F("save-as-template", "Repeat a past workout or save it as a template", "PLAN",
  "Turn a completed workout into a template, or start a new session copied from it.",
  s="i23 i138", h="43 a42", t="95", f="x52", m="74")
F("update-template", "Update template from a workout", "PLAN",
  "After a workout that changed, choose to write the changes back into its template.",
  h="5 a6", t="96", m="77")
F("template-history", "Per-template progress", "PLAN",
  "A template shows its past runs or a progress trend.",
  s="95", m="81 a83")
F("prebuilt-workouts", "Ready-made single workouts", "PLAN",
  "A library of pre-built single sessions to start from.",
  h="82 a83", t="99", f="48", m="80")
F("prebuilt-programs", "Ready-made programs and splits", "PLAN",
  "A library of pre-built multi-day programs or weekly splits.",
  s="79 a80 i110 ai119", h="81", g="13 a15")
F("creator-programs", "Programs from named coaches", "PLAN",
  "Structured plans authored by named coaches or creators, with their own content.",
  g="16")
F("split-builder", "Custom split builder", "PLAN",
  "Build your own multi-day split or weekly plan by hand.",
  s="82 a81 i112 ai109 ai111 ai113 ai114 ai115 ai116 ai117 ai120 ai121 ai122 ai123 ai124 ai213", g="14")
F("training-calendar", "Planning calendar", "PLAN",
  "Schedule workouts on future dates in a calendar, and see planned against completed.",
  s="83 a84 a85 a86 a87 a88 a89 a90 a65 i126 i128 ai127 ai129 ai130 ai131 ai132 ai133", t="57")
F("history-calendar", "Workout history calendar", "PLAN",
  "A calendar or grid view of days you trained.",
  s="i214 x83", h="134 a135", t="x44", g="150", m="120")
F("workout-reminders", "Workout reminders", "PLAN",
  "Notifications reminding you to train (scheduled or after inactivity).",
  s="i267 ai269", f="49", m="123")
F("apple-calendar-sync", "Apple Calendar sync", "PLAN",
  "Planned workouts appear in the system calendar.",
  s="91 i135")

# ---------------------------------------------------------------- PROG
F("plan-generation", "Generated training program", "PROG",
  "The app builds a personalised multi-day program from your goals, schedule and equipment.",
  s="103 a104 a105 a109 i107 ai95",
  h="84 a91 a92 a93 a98 a101 a102 a103 a104 a105 a106 a107 a108 a109 a110 a111 a112 a113",
  g="10 a11 a20 a21 a22 a24 a25 a26 a27 a28 a29 a30 a35 a83",
  f="x0 x11 a7 a8 a9 a10 a11 a12 a13 a14")
F("workout-generation", "Generated single workout", "PROG",
  "The app generates a personalised workout on demand (today's session).",
  s="102 107 i106 ai94", h="x92", g="18 a23", f="0 a1 a16 a17 a18 a41", m="86 a88 a89 a90 a91 a93 a102")
F("progressive-overload", "Automatic progressive overload", "PROG",
  "The app recommends when and how much to increase weight or reps based on your performance.",
  h="85 a86 a87 a88", g="0 a1 a43 a46 a47 a48 a49 a50 a51", f="3 a4 a5 a6", m="96 a97 a99")
F("template-progression", "Progression on repeated templates", "PROG",
  "Saved workouts can be re-run with automatically progressed sets, reps or weights.",
  g="78", f="53", m="98")
F("recovery-planning", "Recovery-driven workout selection", "PROG",
  "The next workout's muscles are chosen from estimated per-muscle recovery.",
  g="12 a111", f="x11 x17 a20", m="87 a84")
F("auto-supersets", "Automatically generated supersets", "PROG",
  "Generated workouts can group exercises into supersets or circuits automatically.",
  g="x62", f="42", m="94")
F("exercise-preferences", "Exercise exclusions and preferences", "PROG",
  "Exclude exercises (or muscles) from recommendations, or ask for some more often.",
  h="96", g="37 38 a36 a39", f="22", m="92")
F("injury-aware", "Injury-aware programming", "PROG",
  "Record injuries or painful movements and recommendations avoid or substitute aggravating exercises.",
  s="106", h="97", g="40 a41", f="23", m="103")
F("equipment-profiles", "Gym equipment profiles", "PROG",
  "Saved gym/equipment profiles restrict recommended exercises to what you have.",
  h="99", g="6 98 a94 a95 a96 a99", f="32 34 a30 a31 a35", m="100")
F("owned-weights", "Available weights and increments", "PROG",
  "Tell the app which dumbbells, plates or machine increments you have so suggestions are loadable.",
  h="100", g="2 97 a100", f="33 a36", m="101")
F("periodization", "Periodization (deloads, phases, test days)", "PROG",
  "Planned variation over weeks: deload periods, phased progressions or max-effort test days.",
  g="34", f="2 15 21")
F("workout-regeneration", "Regenerate today's workout", "PROG",
  "Ask for a new version of a generated workout.",
  g="19", f="19", m="95")
F("weekly-set-targets", "Weekly set targets per muscle", "PROG",
  "Recommended weekly working-set ranges per muscle, with progress against them.",
  h="90 a89", g="x142", f="24")

# ---------------------------------------------------------------- AI
F("ai-coach-chat", "AI coach chat", "AI",
  "A conversational AI coach inside the app that answers using your own training data.",
  s="96 a97 a98 a99 a100 a101 a113 i93 ai96 ai97 ai99 ai100 ai101 ai102 ai103 ai104 ai272 a108 ai98",
  m="104 a105 a106")
F("ai-summaries", "AI-written training summaries", "AI",
  "AI-written plain-language summaries of a workout or a training week.",
  s="110 a111 a112 i105 ai224 ai271", g="52 53")
F("ai-form-analysis", "Form analysis from video", "AI",
  "Record or upload a video of a set and get a form score or feedback.",
  g="54 a55")
F("ai-physique-analysis", "AI progress-photo analysis", "AI",
  "AI commentary on progress photos.",
  s="114 i108")
F("ai-custom-exercise", "AI-filled custom exercises", "AI",
  "AI fills in a custom exercise's details from its name or a video link.",
  s="71 i10", g="92 a91")
F("external-ai", "ChatGPT / Claude / MCP integration", "AI",
  "Connect external AI assistants (ChatGPT, Claude, MCP clients) to your training data.",
  h="114 a115 a116", g="168", m="107 a108")
F("voice-logging", "Voice logging", "AI",
  "Log sets, workouts or plans by speaking.",
  s="116 a117 a118 a119 a120 a121 a122 a123 a66 a133 a134 i90 ai91 ai92 ai118 ai66 ai74")
F("head-gesture-logging", "Head-gesture logging", "AI",
  "Log sets hands-free with head gestures through headphones.",
  f="119")

# ---------------------------------------------------------------- LIB
F("exercise-library", "Built-in exercise library", "LIB",
  "A built-in catalogue of exercises (size as stated by the app).",
  s="67 i6", h="74 a14", t="106", g="x7", f="78 a83 a84 a85 a86 a87 a88 a89", m="64 a68")
F("exercise-demos", "Exercise demonstration videos or animations", "LIB",
  "Each exercise has a video or animated demonstration.",
  s="68 i7", h="75", t="5", g="7", f="79")
F("exercise-instructions", "Written exercise instructions", "LIB",
  "Step-by-step written instructions for exercises.",
  s="x68 xi7", h="76 a47", t="4", g="9", f="80", m="66")
F("exercise-muscle-map", "Target muscles per exercise", "LIB",
  "Shows the primary and secondary muscles an exercise works.",
  s="69", f="81", m="x66")
F("exercise-search", "Exercise search and filters", "LIB",
  "Search the exercise library and filter it by muscle or equipment.",
  s="73 i5", h="x74", t="48", g="88 a89", f="82", m="67")
F("custom-exercises", "Custom exercises", "LIB",
  "Create your own exercises.",
  s="70 a72 i9", h="77 a78 a79", t="0 a59", g="90 a93", f="65", m="69 a70")
F("library-management", "Hide, merge or reset exercise data", "LIB",
  "Hide unwanted library exercises, merge one exercise's history into another, or reset history from a date.",
  t="104 105 61")
F("offline-videos", "Offline exercise videos", "LIB",
  "Download exercise videos to watch without a connection.",
  g="8")
F("warmup-routines", "Warm-up, stretching and mobility routines", "LIB",
  "Stretching, mobility or warm-up exercise routines added before or after workouts.",
  g="66 67", f="38 a39 a40", m="65")
F("app-tutorials", "In-app tutorials and guided setup", "LIB",
  "Built-in or official how-to guidance for using the app.",
  s="246 ai276", m="72")

# ---------------------------------------------------------------- STAT
F("personal-records", "Personal records", "STAT",
  "Personal records are detected automatically, ideally flagged as they happen.",
  s="35 x74 i231 ai219 ai236 ai237", h="120 a122 a123", t="6", g="84 a85 a101", f="94", m="117")
F("rep-max-table", "Records by rep count", "STAT",
  "A table of best (and predicted) weights for each rep count.",
  h="121", t="62 63", m="113")
F("estimated-1rm", "Estimated one-rep max", "STAT",
  "Estimated 1RM calculated from logged sets.",
  s="x74 i230", h="65", t="7", g="44 a45", f="90", m="112")
F("exercise-charts", "Per-exercise progress charts", "STAT",
  "Charts of an exercise's weight, 1RM, volume or reps over time.",
  s="74 i229", h="117 a118", t="18 19 103", g="136", f="95", m="114")
F("exercise-history", "Per-exercise history", "STAT",
  "A list of every past session of a given exercise.",
  s="x74 i232", h="119", t="102", g="137", m="x114")
F("volume-tracking", "Training volume tracking", "STAT",
  "Total volume (weight x reps) calculated per workout and over time.",
  s="173 i218 ai220", h="x133", t="8 a110", f="96", m="111")
F("training-trends", "Workout frequency and duration trends", "STAT",
  "Charts of how often and how long you train over time.",
  s="171 172 a177 i215 ai212 ai216 ai217 ai210", h="133 a130")
F("muscle-breakdown", "Sets or volume per muscle group", "STAT",
  "Stats breaking training down by muscle group.",
  s="169 xi220 xi211", h="125 127 128 129", g="142", f="x24", m="x126")
F("muscle-heatmap", "Muscle heatmap", "STAT",
  "A body diagram shading the muscles trained in a workout or period.",
  s="x180 i13 i211", h="126 a46 a71", t="56", f="29", m="x82")
F("strength-score", "Strength score or level", "STAT",
  "A score or level rating your strength against standards or other users.",
  h="124", g="5 a138 a139 a140 a141", f="91 92 a93 a97")
F("workout-recaps", "Weekly, monthly or yearly recaps", "STAT",
  "Periodic recap reports of your training.",
  s="178 a183 i222 i223 ai270", h="131 132", g="143 a144", f="98 a99 a100")
F("stats-dashboard", "Customisable dashboard", "STAT",
  "Choose which stats, charts or cards appear on a dashboard or home screen.",
  s="235 i208 ai207", t="70 72")
F("workout-summary", "Post-workout summary", "STAT",
  "A summary screen of the finished workout's stats.",
  s="180 i11 ai15", f="x29")
F("volume-comparison", "Real-world volume comparisons", "STAT",
  "Total weight lifted expressed as a real-world comparison.",
  s="218", h="140")
F("training-streak", "Training streaks", "STAT",
  "A streak of consecutive days or weeks of training (or of meeting a weekly goal).",
  s="i170", h="136 a137 a138", t="45 a71", g="157 a158", f="102", m="118 a119 a122")
F("achievements", "Achievements, badges and levels", "STAT",
  "Badges, milestones or levels earned for training.",
  h="139", g="159 a160", f="101", m="116")
F("calories-burned", "Calories burned", "STAT",
  "Active calories recorded or estimated for workouts.",
  s="x126 xi78", h="x141 x220", t="75", g="x122", f="103", m="31 a32")

# ---------------------------------------------------------------- HEALTH
F("apple-health-write", "Workouts written to Apple Health", "HEALTH",
  "Finished workouts are saved to Apple Health.",
  s="150 i160", h="219 a220 a222", t="65", g="113", f="107 a110", m="131")
F("apple-health-import", "Import workouts from Apple Health", "HEALTH",
  "Workouts recorded by other apps are brought in from Apple Health.",
  s="151 i159", t="64", g="114", f="108", m="132")
F("health-body-data", "Body data synced with Apple Health", "HEALTH",
  "Body weight or composition is read from or written to Apple Health.",
  s="i165", h="144", t="66", g="116", f="109 a106", m="133")
F("bodyweight-tracking", "Body weight log", "HEALTH",
  "Log body weight over time with a trend.",
  s="i238 a174 ai221", h="x142", t="22", g="x146", f="104 105")
F("body-measurements", "Body measurements (circumferences, body fat)", "HEALTH",
  "Log body measurements beyond weight, such as circumferences or body-fat %.",
  s="154", h="142 a143 a148", t="21 23 24", g="145 a146 a147", f="x104")
F("progress-photos", "Progress photos", "HEALTH",
  "Store private progress photos over time.",
  s="158 i239 ai240 ai241 ai242 ai243", h="145 a146 a147", t="33", g="148 a149")
F("nutrition-logging", "Calorie and macro logging", "HEALTH",
  "Log food calories or macronutrients.",
  t="25 67 68 69")
F("sleep-tracking", "Sleep tracking", "HEALTH",
  "View sleep (e.g. from Apple Health) or log it.",
  s="152 a153 i162 ai163")
F("steps-tracking", "Steps tracking", "HEALTH",
  "Steps history in the app.",
  s="155 i164")
F("activity-rings", "Activity rings in the app", "HEALTH",
  "Move/Exercise/Stand rings shown inside the app.",
  s="156 a157 i161 ai169")
F("habit-tracking", "Habit and daily-goal tracking", "HEALTH",
  "Track daily habits or a combined daily goal, with streaks and reminders.",
  s="160 a161 a162 a163 a164 i154 ai155 ai156 ai157 ai266 a165 a166 a167 a168 a234 ai166 ai167 ai84 ai265")
F("muscle-recovery", "Muscle recovery tracking", "HEALTH",
  "Per-muscle recovery or fatigue estimates.",
  g="109 a110 a112", f="25 a26 a27 a28", m="109 a110")
F("heart-rate", "Heart rate during workouts", "HEALTH",
  "Heart rate recorded and shown during or after a workout.",
  s="38 i58 ai78", h="194 a141", t="74", g="122", f="124 a116", m="29")
F("hr-zones", "Heart-rate zones", "HEALTH",
  "Time in heart-rate zones for a workout.",
  s="159 i12", m="30")

# ---------------------------------------------------------------- CARDIO
F("cardio-logging", "Cardio exercise logging", "CARDIO",
  "Log cardio with distance and/or time.",
  s="x64", h="9", t="1 109", g="75", f="69", m="x51")
F("activity-types", "Non-lifting activity types", "CARDIO",
  "Track many activity types beyond lifting (sports, yoga, classes, recovery sessions such as sauna).",
  s="52 54 a57 i21 i52 ai22 a63 a175 ai53")
F("multi-activity-session", "Multi-activity sessions", "CARDIO",
  "Chain several activities into one saved session.",
  s="53 i51 ai77")
F("gps-tracking", "GPS outdoor tracking", "CARDIO",
  "Track outdoor runs, walks or rides with GPS distance and pace.",
  s="58 a60 i54 ai79")
F("route-maps", "Route maps", "CARDIO",
  "Outdoor workouts show a route map.",
  s="59 i14", g="115")
F("swim-tracking", "Swim tracking", "CARDIO",
  "Pool laps or open-water swims tracked.",
  s="61 a62 a146 i80 ai57")
F("interval-timers", "Interval and round timers", "CARDIO",
  "Timed intervals for HIIT, Tabata, circuits or boxing rounds.",
  s="7 55 56 i55 i56", f="46 a47")
F("machine-photo-scan", "Read a cardio machine screen by photo", "CARDIO",
  "Photograph a cardio machine's display to import its numbers.",
  s="64 i17")

# ---------------------------------------------------------------- WATCH
F("watch-app", "Apple Watch app", "WATCH",
  "An Apple Watch app for logging strength workouts.",
  s="126 a132 a136 a137 a138 a141 a142 a143 a242 i67 ai62 ai75 ai76 ai81 ai82 ai83 ai88 ai89",
  h="187 a190 a195", t="x2 a47 a58 a77 a78 a80 a84", g="120 a121 a123",
  f="120 a121 a123", m="19 a23")
F("watch-standalone", "Watch logging without the phone", "WATCH",
  "Log a whole workout on the watch without the iPhone nearby.",
  s="149", h="x187 x196", t="2", g="4", m="x27")
F("watch-templates", "Start templates or plans on the watch", "WATCH",
  "Start a saved template, routine or today's planned workout from the watch.",
  s="i64 ai65", h="189 a197", g="126", m="22 a20")
F("watch-phone-sync", "Live phone-watch sync", "WATCH",
  "The same workout is mirrored live on phone and watch.",
  s="135 i85", h="188", t="73 a76", g="125", f="x121", m="21")
F("watch-workout-editing", "Edit workout structure on the watch", "WATCH",
  "Add or delete sets, or add, swap or reorder exercises, from the watch.",
  s="130 a131 a139 i70 ai69 ai71 ai72", t="83 a60 a81 a82", f="122", m="x21 a24")
F("watch-set-types", "Set types and effort on the watch", "WATCH",
  "Tag set types or rate effort from the watch.",
  s="140 i68", h="191", t="79", g="124", f="125", m="41")
F("watch-complications", "Watch complications", "WATCH",
  "App complications or widgets on the watch face.",
  s="144 i86 ai87", h="192", g="128", m="26")
F("watch-faces", "Custom watch faces", "WATCH",
  "App-provided Apple Watch faces.",
  s="145", h="193")
F("auto-rep-counting", "Automatic rep counting", "WATCH",
  "The watch counts reps automatically from motion.",
  s="127 a128 a129 i73", m="1 a11 a18")
F("auto-exercise-detection", "Automatic exercise detection", "WATCH",
  "The watch identifies which exercise you are doing (and when sets start and end) from motion alone.",
  m="0 a2 a3 a4 a5 a6 a7 a8 a9 a10 a12 a13 a14 a15")
F("airpods-heart-rate", "Heart rate from AirPods", "WATCH",
  "Read heart rate from AirPods Pro during workouts.",
  h="198", g="119", f="117")
F("bluetooth-hr", "Bluetooth heart-rate monitors", "WATCH",
  "Connect Bluetooth chest straps or other BLE heart-rate monitors.",
  f="118")
F("garmin-watch-app", "Garmin watch app", "WATCH",
  "An app that runs on Garmin watches to log workouts.",
  g="129")
F("garmin-connect", "Garmin Connect sync", "WATCH",
  "Workouts appear in Garmin Connect.",
  g="130", f="115")
F("wear-os-app", "Wear OS app", "WATCH",
  "An app for Wear OS watches.",
  h="199 a200", g="131 a132", f="126 a127")
F("fitbit", "Fitbit integration", "WATCH",
  "Workouts exchanged with Fitbit.",
  f="114")

# ---------------------------------------------------------------- SOC
F("friends", "Friends or followers", "SOC",
  "Add friends or follow other users.",
  s="184 a190 a191 i171 ai172 ai173 ai178", h="149 a151 a152 a153 a154 a160 a165", g="151",
  m="140 a141 a142 a154")
F("activity-feed", "Activity feed", "SOC",
  "A feed of the workouts of people you follow or are friends with.",
  s="185 i174", h="x149", g="152", m="139")
F("discover-feed", "Community or discover feed", "SOC",
  "A feed or community space beyond your own friends.",
  s="193 a194 i187", h="150")
F("likes-comments", "Likes and comments", "SOC",
  "React to and comment on others' workouts.",
  s="186 i180 ai181", h="155 156 a34 a157 a158", g="153", m="143 144")
F("user-profile", "Customisable profile", "SOC",
  "A user profile with name, photo or bio.",
  s="237 a238 a239 i279", h="163 164 a180")
F("privacy-controls", "Privacy controls", "SOC",
  "Control who can see your activity (private account, per-workout or per-item visibility, hiding from public feeds).",
  s="i188 xi156", h="159 a48 a49", m="149 150 a151")
F("block-report", "Block and report", "SOC",
  "Block users and report users or content.",
  s="198 i189", h="161", m="152 153")
F("live-follow", "Follow a friend's workout live", "SOC",
  "See a friend's workout as it happens.",
  s="187 a210 i175")
F("view-friend-history", "Browse a friend's training", "SOC",
  "Browse a friend's workout history or schedule.",
  s="192 a93 i177 ai134 ai176 ai225", h="x163")
F("friend-compare", "Compare with a friend", "SOC",
  "Compare your stats or lifts side by side with a specific friend.",
  s="176 i179 ai226 ai234", h="168 169", g="155")
F("leaderboards", "Leaderboards", "SOC",
  "Rankings among friends or group members.",
  s="197 i186", h="170", g="154 156")
F("groups", "Groups", "SOC",
  "Private groups of friends with shared activity.",
  s="188 a189 a195 a196 i182 ai184 ai185")
F("competitions", "Competitions and challenges", "SOC",
  "Head-to-head or group competitions over a period.",
  s="200 a201 a202 a203 a204 a205 a206 a207 a208 a209 i190 ai191 ai193 ai194 ai195 ai196 ai197 ai198 ai199 ai200 ai201 ai202 ai203 ai204 ai205 ai206 ai261 ai262",
  m="148")
F("friend-notifications", "Friend activity notifications", "SOC",
  "Notifications when friends work out.",
  s="x143 i260", h="162", m="147")
F("gym-tagging", "Tag a workout's gym or location", "SOC",
  "Attach the gym or location to a workout.",
  h="35", m="x151")
F("trainer-platform", "Connect your personal trainer", "SOC",
  "Link to your own personal trainer, who assigns programs and sees your data.",
  h="182 a183 a184 a185 a186")

# ---------------------------------------------------------------- DATA
F("share-cards", "Shareable workout images", "DATA",
  "Generate shareable image cards of workouts or stats.",
  s="211 a213 a216 i146 ai227 ai235", h="172 a174 a175 a176", g="162", f="137", m="145")
F("instagram-stories", "Share to Instagram Stories", "DATA",
  "Post a workout card directly to Instagram Stories.",
  s="212 xi146", h="173", g="163", m="146")
F("web-workout-links", "Workout web links", "DATA",
  "Share a workout as a web link viewable without the app.",
  s="214 i147 ai284", h="177", f="x137")
F("share-templates", "Share workouts or templates with others", "DATA",
  "Send a template, routine, split or workout to someone who can save and do it.",
  s="215 a77 a94 a217 i142 ai125 ai140 ai141 ai143 ai144 ai145 ai285", h="178 a166 a167 a179",
  t="36 a37", g="161", f="136", m="78 a79")
F("import-history", "Import history from another app", "DATA",
  "Import your workout history from another tracker's export.",
  s="219 a220 i148 ai149 ai150", h="225 a226", g="165", m="136")
F("import-plan-from-media", "Import a workout from photos, files or links", "DATA",
  "Turn screenshots, documents, spreadsheets or social-video links into trackable workouts with AI.",
  s="92 221 222 i151 i152", g="17")
F("data-export", "Data export", "DATA",
  "Export your workout data to a file.",
  s="223 a179 i153 ai228 ai286", h="227 a228", t="38 a39 a40", g="164", m="137 a138")
F("cloud-sync", "Cloud account sync", "DATA",
  "Data is stored in an account and synced across devices.",
  s="x34", h="218", t="20 a114 a115", f="131")
F("strava-export", "Strava export", "DATA",
  "Push finished workouts to Strava.",
  h="223 a224", g="118", f="112", m="135")
F("strava-import", "Strava import", "DATA",
  "Import activities from Strava directly.",
  f="113")
F("health-connect", "Health Connect (Android)", "DATA",
  "Sync with Android Health Connect.",
  h="221", t="117", g="117", f="111")
F("developer-api", "Public developer API", "DATA",
  "A documented API for your own data.",
  g="167")

# ---------------------------------------------------------------- PLAT
F("android-app", "Android app", "PLAT", "Available on Android via Google Play.",
  h="216", t="116", g="169", f="130")
F("ipad-app", "Native iPad app", "PLAT",
  "A native iPad build (universal app listed for iPad on the App Store).",
  h="215")
F("web-app", "Web app or dashboard", "PLAT",
  "Use your account's training data in a web browser.",
  h="217", g="166", f="133")
F("vision-pro", "Apple Vision Pro compatibility", "PLAT",
  "Listed as compatible with Apple Vision on the App Store.",
  g="170", f="132", m="158")
F("mac", "Mac (Apple silicon) availability", "PLAT",
  "Listed as available on Mac on the App Store.",
  f="x132")
F("languages", "Languages other than English", "PLAT",
  "The app is localised into languages other than English.",
  h="72", t="119", g="171", f="134", m="157")
F("home-widgets", "Home and Lock Screen widgets", "PLAT",
  "iPhone Home Screen or Lock Screen widgets.",
  s="224 a225 a226 a227 a228 a229 i247 ai246 ai248 ai249 ai250 ai251 ai252",
  h="205 a206 a207 a208 a209 a210 a211 a212 a213 a214", t="43 44 46 a51", g="133", f="128",
  m="125 a126 a127")
F("live-activity", "Live Activity and Dynamic Island", "PLAT",
  "The live workout appears on the Lock Screen and in the Dynamic Island.",
  s="230 i244", h="201 202", t="41 42", g="134 a135", f="129", m="129")
F("lock-screen-logging", "Log sets from the Lock Screen", "PLAT",
  "Complete sets from the Live Activity without unlocking.",
  s="231 i245", h="203 a204", g="x134", m="130")
F("siri", "Siri and Shortcuts", "PLAT",
  "Control the app with Siri or the Shortcuts app.",
  s="124 a125 i253 i254 ai255", t="55")
F("control-center", "Control Center control", "PLAT",
  "A Control Center button for the app.",
  m="128")
F("imessage-stickers", "iMessage stickers", "PLAT",
  "A sticker pack for Messages.",
  h="181")
F("app-blocking", "Distraction blocking during workouts", "PLAT",
  "Block chosen apps while a workout runs.",
  g="86 a87")
F("no-ads", "No advertising", "PLAT",
  "The app shows no ads.",
  h="73", t="118")

# ---------------------------------------------------------------- PERS
F("dark-mode", "Dark mode", "PERS", "A dark appearance.",
  s="232 i281", h="69 x70", t="54", g="105")
F("themes", "Colour themes and accent colours", "PERS",
  "Choose colour themes or an accent colour.",
  s="233 xi281 ai282", t="52", g="106 107")
F("app-icons", "Alternate app icons", "PERS", "Choose an alternate app icon.",
  t="53", g="108")
F("week-start", "First day of week setting", "PERS", "Choose the day the week starts.",
  s="240 i283", h="68", g="104", f="50", m="121")
F("notification-settings", "Notification controls and inbox", "PERS",
  "Per-type notification toggles, or an in-app notification inbox.",
  s="241 i257 i258 ai259 ai263 ai264", h="231", m="124")
F("sign-in-options", "Sign in with Apple or Google", "PERS",
  "Sign in with Apple or Google accounts.",
  s="243 i275", h="229", t="111 a112", g="173", f="135", m="155")
F("account-deletion", "In-app account deletion", "PERS",
  "Delete your account and data from inside the app.",
  s="244 i280", h="230", t="113", f="140", m="156")
F("in-app-support", "In-app support and feedback", "PERS",
  "Contact the team, report bugs or request features from inside the app.",
  s="115 a199 a245 i273 i274", h="232", g="172 x57")
F("ai-support-assistant", "AI support assistant", "PERS",
  "An AI assistant answers support questions.",
  g="57", f="139")
F("trainer-advice", "Advice from human coaches", "PERS",
  "Ask certified trainers or coaches employed by the app for workout advice.",
  g="56", f="138")

# ---------------------------------------------------------------- vetting
# (app, index-token, class, reason). Index-token uses the same "i" prefix for the SPLYT index.
# Claims not listed here default to `capability` (core or also) or `aspect` (a-token).
VET = [
    # --- SPLYT (data/claims/splyt.json)
    ("splyt", "0", "unsubstantiated", "App Store line still advertises food logging, which SPLYT's own What's New (build 374) and feature index say was removed; set logging is evidenced by other claims instead."),
    ("splyt", "1", "ui_tweak", "Describes the size of the numbers on screen, not a capability."),
    ("splyt", "3", "ui_tweak", "Layout behaviour (one card expanded at a time)."),
    ("splyt", "25", "ui_tweak", "Collapsing a card is a layout control."),
    ("splyt", "41", "ui_tweak", "A banner to return to an open workout is navigation."),
    ("splyt", "42", "ui_tweak", "A 3-2-1 start animation."),
    ("splyt", "49", "ui_tweak", "Draws rest as a line between rows: display option."),
    ("splyt", "128", "unsubstantiated", "On-device/offline rep counting is stated on the website only; the 2026-10-09 feature index does not describe it. Kept as an aspect note only."),
    ("splyt", "147", "ui_tweak", "Watch accent colour following the phone."),
    ("splyt", "148", "ui_tweak", "Clock shows centiseconds."),
    ("splyt", "149", "unsubstantiated", "Website says no phone is needed on the gym floor; SPLYT's own detailed feature index only says the watch starts recording 'without touching your phone', which is not the same as working without it nearby."),
    ("splyt", "151", "capability", "Counts for Apple Health import. Its mention of Strava is not counted as a Strava integration: the feature index says imported workouts come from Apple Health."),
    ("splyt", "154", "unsubstantiated", "Website says 'body weight and measurements'; SPLYT's feature index describes only a body weight log (and weight/steps/sleep trends), no circumference or body-fat logging."),
    ("splyt", "170", "unsubstantiated", "The 0-21 daily strain score appears on the website only; the feature index lists every Stats view in detail and none is a strain score."),
    ("splyt", "182", "ui_tweak", "Press-and-hold on charts is an interaction refinement."),
    ("splyt", "187", "unsubstantiated", "Website says you can watch a friend's sets land live; the feature index describes only a 'training now' live dot. Scored partial on the index."),
    ("splyt", "222", "unsubstantiated", "Release note includes Instagram links; the feature index lists TikTok and YouTube only (Instagram links are rejected). The capability is still evidenced by the index for TikTok/YouTube."),
    ("splyt", "228", "unsubstantiated", "Release note describes a lock-screen widget that starts a workout; the feature index's lock-screen widgets only show rings and open the app."),
    ("splyt", "234", "unsubstantiated", "App Store mention of 'dozens of ring colorways' is not described in the feature index; kept as an aspect only."),
    ("splyt", "236", "ui_tweak", "Tab bar frosting level."),
    # --- SPLYT feature index
    ("splyt", "i41", "ui_tweak", "One-movement-at-a-time is layout."),
    ("splyt", "i48", "ui_tweak", "Minimising the workout to a mini bar is navigation."),
    ("splyt", "i137", "out_of_scope", "Pro tier limit (pricing), excluded by the brief."),
    ("splyt", "i158", "out_of_scope", "Pro tier limit (pricing), excluded by the brief."),
    ("splyt", "i168", "ui_tweak", "Ring fill animation."),
    ("splyt", "i183", "out_of_scope", "Free vs Pro group limits (pricing)."),
    ("splyt", "i192", "out_of_scope", "Free participation in competitions is a pricing statement."),
    ("splyt", "i209", "ui_tweak", "Alternative copy ('roast me') with no new capability."),
    ("splyt", "i256", "ui_tweak", "Universal links opening the app is plumbing, not a user capability."),
    ("splyt", "i277", "out_of_scope", "Subscription management (pricing)."),
    ("splyt", "i278", "out_of_scope", "Pro plans and trial (pricing)."),
    ("splyt", "i287", "ui_tweak", "Invite landing pages are plumbing for friend invites."),
    # --- Hevy
    ("hevy", "29", "ui_tweak", "'Redesigned the Set Row UI ... an RPE color scale' is a redesign."),
    ("hevy", "70", "ui_tweak", "'more haptic feedback, a smoother dark mode experience' is polish."),
    ("hevy", "28", "aspect", "Automatic set checking after RPE entry is a behaviour of RPE logging."),
    # --- Strong
    ("strong", "50", "fix", "'Improved support for the Show Borders accessibility feature' is an improvement to an OS setting."),
    ("strong", "56", "unsubstantiated", "'Muscle Heat Map' appears as a bare name in one of two variants of the homepage feature strip; no help article or release note describes it."),
    ("strong", "57", "unsubstantiated", "Homepage strip lists 'Workout Scheduling', but Strong's help article 'On Future Features' says scheduling is still being worked on."),
    ("strong", "64", "fix", "'Faster Apple Health workout imports' is a performance fix; no Strong source describes the import itself."),
    ("strong", "92", "fix", "'Fix: Timer notifications may not include next set details' is a fix."),
    # --- Gravl
    ("gravl", "61", "fix", "'Fixed Apple Music pausing on rest timer sound' is a fix."),
    ("gravl", "116", "fix", "'Improvements on bodyweight sync from Apple Health' is an improvement; no Gravl source describes the sync itself."),
    ("gravl", "127", "fix", "'Rebuilt Apple Watch experience: better synchronization... more reliable rest timers' is a rebuild/fix."),
    ("gravl", "4", "unsubstantiated", "App Store calls the watch app standalone; Gravl's help article says 'Keep the iPhone within reach: the app on the phone is still what owns and saves the session.'"),
    ("gravl", "85", "aspect", "Named in a list in a release note; kept as an aspect of PR detection."),
    ("gravl", "147", "aspect", "Named in a list in a release note; kept as an aspect."),
    # --- Fitbod
    ("fitbod", "115", "unsubstantiated", "Website FAQ 'Wearable Sync: ... Garmin' only; the help centre documents Garmin only as a Bluetooth heart-rate broadcaster on Android."),
    ("fitbod", "116", "not_shipped", "'Now gradually rolling out on Android and iOS.'"),
    ("fitbod", "97", "not_shipped", "Help says percentile ranking is rolling out gradually; kept as an aspect."),
    # --- Motra
    ("motra", "16", "fix", "'Improvements to auto-detection memory' is an improvement."),
    ("motra", "17", "unsubstantiated", "'provide form-feedback' appears once on a marketing page; no help article describes any form feedback."),
    ("motra", "25", "ui_tweak", "Expand/collapse exercises on the watch is layout."),
    ("motra", "33", "fix", "'we've made some improvements to the phone-only workout' is an improvement note."),
    ("motra", "50", "ui_tweak", "Hiding weight fields for non-weighted exercises is a display change."),
    ("motra", "85", "vague", "'Guide Mode assists with the next set' does not say what it does."),
    ("motra", "115", "vague", "'Track your progress in detail, compare performance over time' describes no specific capability."),
    ("motra", "134", "ui_tweak", "A banner showing Health sync status."),
    ("motra", "148", "vague", "'Challenges' appear only as a notification category; no Motra source describes the feature."),
    ("motra", "104", "not_shipped", "Release 6.3.0 announced the AI Coach as a staged rollout; no help article documents it."),
]

# Claims rejected outright and not attached to any feature (they still appear in vetting.json).
UNATTACHED = {
    "splyt": ["1", "3", "25", "41", "42", "49", "147", "148", "182", "236", "i41", "i48", "i137", "i158",
              "i168", "i183", "i192", "i209", "i256", "i277", "i278", "i287"],
    "hevy": ["29", "70"],
    "strong": ["50"],
    "gravl": ["127"],
    "fitbod": [],
    "motra": ["16", "25", "50", "85", "115", "134"],
}
# Motra 17 (form feedback from wrist motion) is not the same capability as video form analysis,
# and no other app claims motion-based form feedback, so it is logged without a feature.
UNATTACHED["motra"].append("17")
# SPLYT 170 (daily strain score) was the only claim for that feature and is unsubstantiated, so the
# feature was dropped: a row exists only if some app has counted evidence for it.
UNATTACHED["splyt"].append("170")

# ---------------------------------------------------------------- cell overrides
# value, note, evidence (quote, url, sourceType, date) — evidence None means "use best mapped claim".
LOOKUP = "https://apps.apple.com/us/app/id{}"
IDS = dict(splyt=6755893717, hevy=1458862350, strong=464254577, gravl=6450921637, fitbod=1041517543, motra=1548577496)
COMPAT = {
    "splyt": "iPhone Requires iOS 16.4 or later. iPad Requires iPadOS 16.4 or later. Apple Vision Requires visionOS 1.0 or later. Apple Watch Requires watchOS 10.0 or later. Languages English",
    "hevy": "iPhone Requires iOS 15.1 or later. iPad Requires iPadOS 15.1 or later. iPod touch Requires iOS 15.1 or later. Apple Vision Requires visionOS 1.0 or later. Apple Watch Requires watchOS 8.0 or later.",
    "strong": "iPhone Requires iOS 15.0 or later. iPod touch Requires iOS 15.0 or later. Apple Watch Requires watchOS 10.0 or later.",
    "gravl": "iPhone Requires iOS 16.4 or later. Apple Vision Requires visionOS 1.0 or later. Apple Watch Requires watchOS 10.0 or later.",
    "fitbod": "iPhone Requires iOS 18.0 or later. Mac Requires macOS 15.0 or later and a Mac with Apple M1 chip or later. Apple Vision Requires visionOS 2.0 or later. Apple Watch Requires watchOS 10.0 or later.",
    "motra": "iPhone Requires iOS 17.0 or later. Apple Vision Requires visionOS 1.0 or later. Apple Watch Requires watchOS 10.0 or later.",
}


def compat(app, note_value, note):
    return (note_value, note, dict(quote="Compatibility: " + COMPAT[app], url=LOOKUP.format(IDS[app]),
                                   sourceType="app_store", date="2026-10-09"))


OVERRIDES = {}
for a in IDS:
    has_ipad = a in ("splyt", "hevy")
    has_vision = a != "strong"
    has_mac = a == "fitbod"
    OVERRIDES[("ipad-app", a)] = compat(a, "yes" if has_ipad else "no",
        "App Store product page lists iPad" + (" and the store record marks the app universal (iosUniversal)." if has_ipad else " nowhere and the store record is not universal: there is no native iPad version.")
        + (" Fitbod's help centre also says: 'We don't currently support iPad.'" if a == "fitbod" else ""))
    OVERRIDES[("vision-pro", a)] = compat(a, "yes" if has_vision else "no",
        "App Store compatibility " + ("lists Apple Vision." if has_vision else "does not list Apple Vision."))
    OVERRIDES[("mac", a)] = compat(a, "yes" if has_mac else "no",
        "App Store compatibility " + ("lists Mac (Apple silicon)." if has_mac else "does not list Mac."))
OVERRIDES[("languages", "splyt")] = compat("splyt", "no", "App Store lists English as the only language.")

OVERRIDES.update({
    ("android-app", "splyt"): ("no", "No Google Play listing: a Google Play search for 'splyt' and 'splyt fitness' (2026-10-09) returns no SPLYT app.",
        dict(quote="(no SPLYT listing in Google Play search results)", url="https://play.google.com/store/search?q=splyt&c=apps&hl=en_US&gl=US", sourceType="google_play", date="2026-10-09")),
    ("android-app", "motra"): ("no", "No Google Play listing for Motra (motra.com). The only 'MOTRA' result (com.motra.app) is a different developer (motraapp.com). Motra's own help describes iPhone and Apple Watch only.",
        dict(quote="(no Motra/motra.com listing in Google Play search results)", url="https://play.google.com/store/search?q=train%20fitness%20motra&c=apps&hl=en_US&gl=US", sourceType="google_play", date="2026-10-09")),
    ("garmin-watch-app", "hevy"): ("no", "Hevy's help centre says Garmin integration is not possible.",
        dict(quote="We would like to integrate with Garmin, but it is not possible at this time.", url="https://help.hevyapp.com/hc/en-us/articles/35361029194647-Hevy-and-Garmin-Integration-Update-Why-It-s-Not-Possible-Yet", sourceType="help_centre", date="2026-10-07")),
    ("garmin-connect", "hevy"): ("no", "Hevy's help centre says Garmin integration is not possible.",
        dict(quote="We would like to integrate with Garmin, but it is not possible at this time.", url="https://help.hevyapp.com/hc/en-us/articles/35361029194647-Hevy-and-Garmin-Integration-Update-Why-It-s-Not-Possible-Yet", sourceType="help_centre", date="2026-10-07")),
    ("garmin-connect", "fitbod"): ("unknown", "Only the website FAQ quick-stats list Garmin under 'Wearable Sync'; the help centre documents Garmin only as a Bluetooth heart-rate broadcaster on Android. Treated as unsubstantiated.", None),
    ("training-calendar", "hevy"): ("no", "Hevy's calendar shows past workouts only.",
        dict(quote="Important note: the calendar feature cannot be used to plan out which days you intend to complete workouts.", url="https://help.hevyapp.com/hc/en-us/articles/35380117933207-Track-Your-Workout-Consistency-with-the-Calendar-and-Streak-Features", sourceType="help_centre", date=None)),
    ("training-calendar", "strong"): ("no", "The homepage strip lists 'Workout Scheduling', but Strong's help says it is still being built.",
        dict(quote="Currently we're working on... Architectural Overhaul for the next generation of Strong. This directly or indirectly addresses multiple feature requests we've received (in particular Scheduling)", url="https://help.strongapp.io/article/242-future-features", sourceType="help_centre", date=None)),
    ("web-app", "strong"): ("no", "Strong's help lists a web app as in development.",
        dict(quote="Web App. This is also built upon the new architecture and is being worked on at the same time.", url="https://help.strongapp.io/article/242-future-features", sourceType="help_centre", date=None)),
    ("web-app", "fitbod"): ("partial", "Fitbod's website offers a public workout generator, but its own FAQ says the web platform is for onboarding only; you cannot use your training data there.",
        dict(quote="Platforms: iOS, Android and Web for on-boarding purposes only", url="https://fitbod.me/faqs/", sourceType="website", date=None)),
    ("watch-standalone", "gravl"): ("no", "App Store copy calls the watch app standalone, but Gravl's help says the phone must be within reach.",
        dict(quote="Keep the iPhone within reach: the app on the phone is still what owns and saves the session.", url="https://gravl.ai/help/gravl-on-your-apple-watch", sourceType="help_centre", date=None)),
    ("watch-standalone", "fitbod"): ("no", "Fitbod's help says the watch app is a companion.",
        dict(quote="Fitbod for Apple Watch is designed as a companion app, not a standalone experience.", url="https://help.fitbod.me/hc/en-us/articles/360006499194-Apple-Watch", sourceType="help_centre", date=None)),
    ("watch-standalone", "splyt"): ("unknown", "The website says no phone is needed; SPLYT's detailed feature index says only that the watch starts recording 'without touching your phone'. Not enough to confirm logging with the phone away.", None),
    ("watch-templates", "fitbod"): ("no", "Workouts must be started on the iPhone.",
        dict(quote="What requires your iPhone - Starting a workout: Your watch will prompt \"Start workout on your iPhone\"", url="https://help.fitbod.me/hc/en-us/articles/360006499194-Apple-Watch", sourceType="help_centre", date=None)),
    ("watch-workout-editing", "fitbod"): ("partial", "Sets can be added or removed on the watch, but swapping or adding exercises requires the iPhone.",
        dict(quote="Add or remove sets during a workout (up to 9 sets per exercise) ... What requires your iPhone ... Swapping or adding exercises during an in-progress workout", url="https://help.fitbod.me/hc/en-us/articles/360006499194-Apple-Watch", sourceType="help_centre", date=None)),
    ("offline-videos", "fitbod"): ("no", "Fitbod's help says offline video is unavailable.",
        dict(quote="GIFs were removed in a recent update, and offline video support is currently unavailable.", url="https://help.fitbod.me/hc/en-us/articles/30721437384215-How-to-Navigate-the-Exercise-Details-Screen", sourceType="help_centre", date=None)),
    ("nutrition-logging", "splyt"): ("no", "Removed in build 374.",
        dict(quote="Food and calorie logging has been removed. Splyt is focused on training, sleep and recovery.", url="https://splyt.fit (in-app What's New, build 374)", sourceType="release_notes", date="2026-08-15")),
    ("fitbit", "fitbod"): ("partial", "Fitbod can still post workouts to Fitbit and import Fitbit cardio (iOS only), but Fitbit no longer auto-syncs Fitbod workouts into Fitbit activities.",
        dict(quote="Fitbit no longer auto-syncs Fitbod workouts to Fitbit activities. You will need to manually add your Fitbod activities to Fitbit.", url="https://help.fitbod.me/hc/en-us/articles/360026522774-Connecting-Fitbit-to-Fitbod-iOS-Only", sourceType="help_centre", date=None)),
    ("airpods-heart-rate", "fitbod"): ("partial", "Live heart rate (including AirPods Pro 3) is 'gradually rolling out' per Fitbod's own help article.", None),
    ("bluetooth-hr", "fitbod"): ("partial", "Android only, and part of live heart rate, which is still 'gradually rolling out'. Not available on iPhone.", None),
    ("live-activity", "strong"): ("partial", "Strong's Live Activity and Dynamic Island show the rest timer only, not the live workout.", None),
    ("import-history", "gravl"): ("partial", "Only by emailing Gravl support, who import it for you; there is no self-serve importer.", None),
    ("ai-coach-chat", "motra"): ("partial", "Announced in release 6.3.0 (2026-05-22) as a staged rollout 'in the coming week'; no help article documents it, so availability to all users is unconfirmed.", None),
    ("live-follow", "splyt"): ("partial", "SPLYT's feature index describes a live 'training now' dot only; the website's claim that you can watch a friend's sets land live is not in the index.", None),
    ("competitions", "motra"): ("unknown", "'Challenges' appear only as a notification-settings category; no Motra source describes the feature.", None),
    ("muscle-heatmap", "strong"): ("unknown", "Named only in one variant of the homepage feature strip; not described anywhere else.", None),
    ("leaderboards", "fitbod"): ("unknown", "Fitbod 'Clubs' (gym leaderboards) is 'currently in beta at select gym locations' and was excluded at extraction.", None),
    ("body-measurements", "splyt"): ("unknown", "Website says 'body weight and measurements', but the feature index describes a body weight log only.", None),
    ("tempo-tracking", "motra"): ("yes", "Named in a help-centre sentence listing what can be tracked from the watch; no further detail.", None),
})

OVERRIDES[("voice-logging", "gravl")] = ("partial", "Gravl's help says workouts can be described out loud, but the feature is labelled Beta (publicly offered in the app). Not in the extracted claims because the brief excluded beta items; added here as partial.",
    dict(quote="The same sheet also offers Voice and Text, both in Beta, if you'd rather describe your session out loud or type it out.", url="https://gravl.ai/help/create-a-one-time-custom-workout", sourceType="help_centre", date=None))
OVERRIDES[("import-plan-from-media", "fitbod")] = ("partial", "Fitbod can import a workout from a photo or screenshot on Android only; not on iPhone.",
    dict(quote="Import Workouts (Android only) Import a workout from a photo or screenshot.", url="https://help.fitbod.me/hc/en-us/articles/38318585683991-Customizing-Today-s-Workout", sourceType="help_centre", date=None))
