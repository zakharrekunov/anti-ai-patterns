# Structures to Avoid

Структурные паттерны. Удаляются вместе с фразами.

## Binary Contrasts

False drama. Скажи Y напрямую.

| Pattern | Problem |
|---------|---------|
| "Not because X. Because Y." / "Not because X, but because Y." | Telegraphed reversal |
| "[X] isn't the problem. [Y] is." | Formulaic reframe |
| "The answer isn't X. It's Y." | Predictable pivot |
| "It feels like X. It's actually Y." | Setup/reveal cliche |
| "The question isn't X. It's Y." | Rhetorical misdirection |
| "Not X. But Y." / "not X, it's Y" / "isn't X, it's Y" | Mechanical contrast |
| "It's not this. It's that." | Same formula |
| "stops being X and starts being Y" | False transformation arc |
| "doesn't mean X, but actually Y" | Negation-then-assertion crutch |
| "is about X but not Y" | False distinction |
| "not just X but also Y" | Additive hedge |
| "Не X, а Y." | RU version |
| "Дело не в X, дело в Y." | RU version |
| "Это не [X]. Это [Y]." | RU version |

**Fix:** скажи Y. "The problem is Y." / "Проблема в Y."

## Negative Listing

Rhetorical striptease через отрицания.

| Pattern | Problem |
|---------|---------|
| "Not a X... Not a Y... A Z." | Dramatic buildup |
| "It wasn't X. It wasn't Y. It was Z." | Same, past tense |
| "Не X. Не Y. Это Z." | RU version |

**Fix:** скажи Z сразу.

## Dramatic Fragmentation

Sentence fragments = manufactured profundity.

| Pattern | Problem |
|---------|---------|
| "[Noun]. That's it. That's the [thing]." | Performative simplicity |
| "X. And Y. And Z." | Staccato drama |
| "This unlocks something. [Word]." | Artificial revelation |
| "Скорость. Качество. Цена." | RU staccato |

**Fix:** полные предложения. Trust content over presentation.

## Rhetorical Setups

Анонсируют insight вместо доставки.

| Pattern | Problem |
|---------|---------|
| "What if [reframe]?" | Socratic posturing |
| "Here's what I mean:" | Redundant preview |
| "Think about it:" | Condescending prompt |
| "And that's okay." | Unnecessary permission |
| "Представьте" | RU posturing |
| "А что если..." | RU socratic |
| "Задумайтесь" | RU condescending |
| "И это нормально." | RU permission |

**Fix:** скажи point. Reader выводы сделает сам.

## Formulaic Constructions

| Pattern | Problem |
|---------|---------|
| "By the time X, I was Y." | Narrative template |
| "X that isn't Y" | Indirect. Say "X is broken" |
| "To my surprise, X" | Manufactured arc |

## False Agency

Inanimate things с human verbs. AI обожает потому что избегает naming actor.

| Pattern | Problem |
|---------|---------|
| "a complaint becomes a fix" | Someone fixed it |
| "a bet lives or dies in days" | Someone shipped/killed |
| "the decision emerges" | Someone decides |
| "the culture shifts" | People change behavior |
| "the conversation moves toward" | Someone steers |
| "the data tells us" | Someone reads, concludes |
| "the market rewards" | Buyers pay |
| "решение приходит" | RU |
| "культура меняется" | RU |
| "данные говорят" | RU |
| "рынок поощряет" | RU |

**Fix:** назови человека. "The team fixed it that week" / "Команда зафиксила за неделю". Если нет конкретного — `you`.

## Narrator-from-a-Distance

Над сценой, не в ней.

| Pattern | Problem |
|---------|---------|
| "Nobody designed this." | Disembodied |
| "This happens because..." | Lecturer voice |
| "This is why..." | Same |
| "People tend to..." | Armchair sociologist |
| "Никто не задумывал" | RU |
| "Так происходит потому что" | RU |
| "Люди склонны" | RU |

**Fix:** поставь читателя в комнату. `You` beats `People`. "You don't sit down one day and decide to..." beats "Nobody designed this."

## Passive Voice

Скрывает actor, тянет энергию. Каждое предложение должно иметь subject делающий action.

| Pattern | Fix |
|---------|-----|
| "X was created" | Name who created |
| "It is believed that" | Name who believes |
| "Mistakes were made" | Name who made |
| "The decision was reached" | Name who decided |
| "Было решено" | Кто решил |
| "Считается что" | Кто считает |
| "Принято считать" | Кто принял |

## Sentence Starters to Avoid

| Pattern | Fix |
|---------|-----|
| What, When, Where, Which, Who, Why, How в начале | Restructure |
| Paragraphs starting with "So" / "Итак" | Start with content |
| "Look," / "Слушайте," | Remove |

Wh-openers становятся crutch. "What makes this hard is..." → "The constraint is..." → лучше: назови constraint.

## Rhythm Patterns

| Pattern | Fix |
|---------|-----|
| Three-item lists everywhere | Two items or one |
| Questions answered immediately | Let breathe or cut |
| Every paragraph ends punchy | Vary endings |
| Em-dashes (— –) | Remove. Commas/periods. ZERO em-dashes. |
| Staccato fragmentation | Don't stack short punchy sentences |
| "Not always. Not perfectly." | Hedging-as-reassurance |
| Parallel triplet ("the one X, the one Y, the one Z") | Vary syntax |

## Word Patterns

| Pattern | Problem |
|---------|---------|
| Lazy extremes (every, always, never, everyone, всегда, никогда) | False authority |
| Скопление adverbs, 2-3 в абзаце (см. phrases.md) | Empty emphasis |
| Quotation marks вокруг фраз | AI tell (см. Rule 2) |

## Хвост значимости

Предложение закончено, а модель добавляет деепричастный или -ing оборот, который объясняет, почему это важно.

| До | После |
|---|---|
| "The app logs every dose, giving users a clear picture of their progress." | "The app logs every dose. You can see the last 30 days on one screen." |
| «Мы добавили напоминания, обеспечивая пользователям бесшовный опыт.» | «Мы добавили напоминания: приложение пишет в 9 утра, если доза не отмечена.» |

Режь хвост. Если в нём была настоящая мысль, дай ей отдельное предложение с конкретным следствием.

## Синонимы по кругу

Модель приучена не повторять слово и меняет имя одной вещи: «приложение… платформа… сервис… решение», "the app… the platform… the tool… the solution". Читатель гадает, одна это вещь или четыре. Выбери одно имя и повторяй его.

## Мораль в конце абзаца

| Паттерн | Fix |
|---|---|
| "Ultimately, it's about…" / «В конечном счёте, всё сводится к…» | Закончи на последнем факте |
| "By doing X, you'll Y." / «Делая X, вы получите Y.» | Удали, если Y уже видно из абзаца |
| "In conclusion" / «Подводя итог» | Удали, итог не пересказывай |
