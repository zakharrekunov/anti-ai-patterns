# Zak-specific Hard Rules

Правила из реальных ревью автора: посты и комментарии на Reddit, LinkedIn, письма. Каждое имеет историю, пробивали уже в проде, теперь стандарт.

---

## Rule 1 — No dashes (— –)

**Запрет:** em-dash и en-dash в любом human-facing тексте (посты, комменты, DMs, newsletters, pitches, ads).

**Why:** AI tell. Forum-native writing использует запятые, точки, скобки, новые предложения. Dashes читаются "polished/edited".

**Fix:**
- лёгкая пауза → запятая
- жёсткий разрыв → точка
- aside → скобки
- иначе перепиши предложение

**Hyphens в составных словах OK:** `zombie-meds`, `follow-up`, `day-to-day`.

---

## Rule 2 — No quotes-for-emphasis (`"..."`)

**Запрет:** двойные кавычки вокруг короткой фразы для выделения, примера, концепта, inner monologue.

**Why:** AI оборачивает фрагменты в кавычки чтобы пометить их концептами. Живые люди интегрируют фразу в поток.

**Bad → Good:**
- `"Felt foggy today" was a typical entry` → `A typical entry was felt foggy today`
- `not "clean my room", just one thing` → `not cleaning the room, just one thing`
- `reading posts and thinking "okay but HOW"` → `reading posts and thinking okay but how`

**Acceptable exception:** atributed quote другого спикера с реальной narrative цели (редко).

---

## Rule 3 — No uniform closing-question

**Запрет:**
- `I'm curious what it was like for other people…` + compound question
- `I'd love to hear how others approached this. Was it more like X or more like Y?`
- любая bifurcated `Was it A, or more of B? And did C or D?`
- закрывать **каждый** пост в batch'е вопросом

**Why:** 2026-05-27 review пачки Reddit-постов: 8 из 13 постов кончались вопросом, 5 формулой "I'm curious". Uniform pattern = AI signature даже когда индивидуальный пост ок.

**Rules:**
1. Default — close on statement, trailing thought, "I don't know"
2. No `I'm curious`/`I'd be curious`/`I wonder if other people` для closing
3. No compound/bifurcated questions. Один open question если уж нужно
4. Question-driven post: вопрос В ТЕЛЕ, не в конце. Конец = statement о том что не понятно
5. Batch 5+: max 2-3 ending on question
6. No parallel-rhythm setup ("the one you'd built…, the one that held…, the one…" + question = AI triplet)

**Good closes:**
- "the part i still don't have a handle on is whether the drift was the medication doing its actual job, or whether the medication was over and i hadn't clocked it"
- "i don't have a clean answer for how that transition felt from the inside"
- "what i don't get is how the old explanation actually loses its grip"

---

## Rule 4 — No "for people who X, [question]" opener

**Запрет:** `for people who [X], [Y]?` / `Для тех, кто [X], [Y]?` как title или question opener.

**Why:** 2026-05-27 review — встречалось 4+ раз в batch'е. Читается как marketing audience targeting. Real Redditors не сегментируют формально, вшивают аудиторию в сам вопрос.

**Replace patterns:**

1. Direct, audience implied:
   - ❌ `for people who came off, what was the signal`
   - ✓ `when did you actually know it was time to come off`

2. Observational (что заметил в сабе):
   - ❌ `for people who got diagnosed with depression first, what made you start considering bipolar`
   - ✓ `the depression-to-bipolar diagnosis flip, when did it actually click for you`
   - ✓ `anyone here who started with a depression diagnosis and only later got bipolar, what shifted`

3. Personal curiosity:
   - ❌ `for people who tried bupropion after SSRI, how did you decide`
   - ✓ `how does the SSRI-to-bupropion switch decision actually get made`
   - ✓ `i keep wondering how people end up on bupropion instead of staying on an SSRI`

4. Question as title, no preamble:
   - ✓ `what made it click that you needed to stop`
   - ✓ `the taper decision, was it a moment or a drift`

**Batch rule:** ZERO постов в batch'е с `for people…`. Multi-post → разные синтаксические подходы.

---

## Rule 5 — No scientific jargon в casual content

**Запрет:** `n=1`, `p-value`, `control group`, `anecdata`, `external validation`, `confirmation bias` (как casual disclaimer), `statistically significant`, `self-reported data`, `methodology` в peer-to-peer subreddit постах.

**Why:** 2026-05-27 review QS draft. Даже в data-loving сабах живые посты имеют narrative и личность. "n=1 breakdown" читается как polished AI mimicking analyst.

**Replace:**

| Banned | Use |
|--------|-----|
| `n=1` | `just my experience` / `in my case` / drop |
| `external validation` | `no way to know if I'm right` / `could be wrong` |
| `confirmation bias` (disclaimer) | `might be reading too much into it` |
| `control group` | `didn't compare to anything` |
| `anecdata` | `just one story` |
| `statistically significant` | `noticeable` / `real` |
| `self-reported data` | `what I wrote down` |
| `methodology` (casual) | `what I tried` / `the approach` |

**OK где:** internal research docs, technical posts в technical субах где явно делаешь science. NOT в обычных subreddit постах даже в data-adjacent сабах.

---

## Rule 6 — No outsider-disclosure opener

**Запрет:** открывать пост с `I'm posting from outside`, `I'm not [tribe], but…`, `I was on X, not Y`, `I never tried [drug], so I'm coming at this from outside`.

**Why:** 2026-05-27 review пачки постов: 4 из 5 постов начинались с outsider disclosure. Reader scroll-fast → если первая строка "I'm not really one of you", уходит. Outsider position нужно ЗАСЛУЖИТЬ в посте, не объявлять upfront.

**Fix:**

Веди **observation/pattern/question** — тем, что интересно. Personal context (включая outsider) вшивай во 2-3 параграф, где служит вопросу.

**Bad (BipolarReddit):**
> "I'm posting this from outside. I was treated for depression, was on an SSRI for about two years…"

**Good:**
> "The thing I keep not being able to picture is the diagnosis flip. A lot of posts here describe a point when their depression diagnosis got revised to bipolar or bp2, and the way they describe it sounds less like a correction and more like a reframe of years…"
> [para 2-3]: "Coming at this from the depression side, I'd been on an SSRI for two years, off now…"

**Bad (Effexor):**
> "I was on an SSRI, not Effexor. Tapered off a few months ago…"

**Good:**
> "The tapering posts here have a specific shape. Someone describes what their prescriber suggested… Then what they actually ended up doing…"
> [later]: "My own taper was for an SSRI, not Effexor, so I'm comparing across…"

**Exception:** если не флагать = deceptive, флагай — но ПОСЛЕ хука, не первой строкой.

---

## Rule 7 — No "The X..." sentence openers

**Запрет:** начинать sentences с `The [noun]...` в peer/forum контенте.

**Why:** 2026-06-11 review ответа на Reddit. Open with article + noun читается polished/AI. Real Redditors дропают article, начинают subject directly, conjunction'ом, verb'ом или concrete noun без "the".

**Bad → Good:**
- `The trying-to-avoid-APs thing happens here a lot` → `Trying to avoid APs and ending up on one happens a lot`
- `The mood-stabilizing side of Vraylar matters more` → `Mood-stabilizing side of Vraylar matters more`
- `The drug isn't doing what you needed` → `It wasn't doing the job you needed`

**Acceptable:** "The" не в начале предложения. "The DXM piece" / "the new psych" внутри предложения нормально.

---

## Rule 8 — No hyphenated compound modifier sprinkle

**Запрет:** sprinkling hyphen-glued compound modifiers через текст. `first-line`, `mood-stabilizing`, `volume-knob`, `anxiety-improvement`, `PCP-misprescription`, `depression-adjunct`, `top-of-mind`, `peer-mod`.

**Why:** 2026-06-11 review. Hyphenated compounds в peer comment чтении clinical/AI. Один-два на длинный пост ok если это стандартное phrase (off-label, follow-up). Sprinkle = AI tell.

**Hard cap:** max 0-1 hyphen-compound modifier per reply, и только если это уже стандартная phrase в casual English.

**Bad → Good:**
- `first-line anxiety thing` → `first thing they'd reach for`
- `mood-stabilizing side` → `the part that handles mood`
- `volume-knob metaphor` → `dial metaphor` или dial без слова
- `anxiety-improvement` → `improvement in anxiety` or just `improvement`
- `depression-adjunct` → `used with antidepressants`

**OK:** off-label, follow-up, well-known, day-to-day (standard hyphenated phrases). One per reply ceiling.

---

## Rule 9 — No point-by-point coverage of commenter's reply

**Запрет:** ответ который addresses каждый пункт коммента one-by-one, paragraph per point, coverage symmetry.

**Why:** 2026-06-11 review. AI synthesizes полную coverage commenter's content. Humans pick 1-2 things that actually matter, отвечают на них, остальное оставляют implicit.

**Anti-pattern:** commenter упоминул 5 фактов → ваш reply имеет 5 paragraphs/sections адресующих каждый. Symmetric coverage = AI signature даже если individual sentences ok.

**Fix:** read commenter's reply, identify 1-2 most useful things to respond on (validation, plain-language answer to direct question, one clear practical takeaway). Drop the rest. If they wrote details that don't need response, leave them unaddressed — that's how peers reply.

**Bad structure (synthesizer mode):**
- ¶1: address fact A
- ¶2: address fact B
- ¶3: address fact C
- ¶4: answer their direct question
- ¶5: summary/closing validation

**Good structure (peer mode):**
- ¶1: react to the 1 thing that matters most
- ¶2: answer their direct question if they asked one
- short close

---

## Применение

Rules 1-6 применяются ко **всему тексту наружу**: Reddit, LinkedIn, Substack, email, community, DMs, документы для команды. Rules 7-9 к тексту от лица человека: Reddit-посты и комменты, DM, ответ в письме. В рекламном тексте Rules 3 и 4 не действуют, см. рекламный режим в SKILL.md.

Batch review: при выдаче 5+ items одновременно проверяй uniform pattern — если все 5 закрываются вопросом или 3 открываются "for people…" → пересобирай batch.
