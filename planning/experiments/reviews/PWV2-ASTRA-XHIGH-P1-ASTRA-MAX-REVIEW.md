# Experimental Independent Review — Astra Max over Astra XHigh PWV2-P1

Date: 2026-09-22
Status: green
Experiment ID: `PWV2-ASTRA-XHIGH-P1-ASTRA-MAX-REVIEW`

## Purpose

Run an isolated, non-canonical independent review of the exact Astra XHigh Strategic Master Plan using Astra Max.

This is **not** the canonical Project Workflow V1 Stage-6 Plan Review. It exists only to obtain an additional independent high-reasoning critique for later comparison/meta-synthesis.

The canonical `feat/common-preexecution-core` workstream and canonical `planning/reviews/PWV2-P1.md` must remain untouched.

## Execution surface

- reviewer surface: Codex / Astra Max
- review role: experimental independent reviewer
- canonical V1 route selection does not govern reviewer eligibility for this experiment
- do not reinterpret this experiment as `codex_only`, `mixed`, or a canonical Project Workflow route
- V1 Plan Review semantics may be used as review-quality guidance only; its normal-ChatGPT reviewer-identity requirement is intentionally not the authority for this isolated experiment

## Exact immutable review subject

Review exactly:

`planning/PROJECT_WORKFLOW_V2_MASTER_PLAN.md@blob:0d55b03e2a4d1a2b1a4fd9972f8365f693262503`

Subject commit:

`4b8d2eefa04ea7511edd92e1799e0fd641f57428`

Do not review a newer branch-tip plan accidentally.

## Frozen Definition authority

Use Definition checkpoint:

`8055ed00acdb708c79919d470217fd87c920973a`

Required authority:
- `requirements/PROJECT_WORKFLOW_V2.md` R1, PWV2-REQ-001..076
- ADR-PWV2-001..006
- `brainstorming/V1_TO_V2_COVERAGE_MATRIX.md`
- `brainstorming/V2_VALIDATION_MATRIX.md`
- `implementation/workstreams/feature-common-preexecution-core/handoffs/DEFINITION_COMPLETE_2026-09-22.md`

## Independence and blindness rules

The reviewer MUST NOT:
- read the ChatGPT experimental plan;
- read blind A/B judge results or reveal;
- read ChatGPT review output;
- read any later canonical Plan Review verdict;
- compare models;
- infer which model is expected to win;
- modify the reviewed plan;
- modify canonical workstream/review state;
- write to `elmakus/project_workflow_v2`.

The reviewed plan is known to have been authored by Astra XHigh only because that is the experiment subject. Do not treat shared model family as favorable evidence.

## Review scope

Perform a full independent strategic review of the immutable plan against frozen Definition authority.

Audit at minimum:
- real coverage of PWV2-REQ-001..076;
- ADR-PWV2-001..006 fidelity;
- full 97-row V1->V2 salvage/regression accounting and explicit DROP assertions;
- A01-A17 and L01-L09;
- milestone sequencing and dependency logic;
- false assumptions / P0-P1 risks;
- plugin/Skill/bootstrap feasibility timing;
- construction control/custody between V1 control repo and V2 implementation repo;
- one-project/one-repository invariant versus bounded construction exception;
- migration/cutover, idempotency, crash recovery and rollback;
- external side effects and uncertain-effect readback;
- review independence and premium A/B/C semantics;
- target movement, source-branch deletion and terminal recovery;
- stacked workstream integration;
- GitHub tracker lifecycle;
- single active Project Card and runtime-owned internal topology;
- delegated implementation semantics;
- Research/prior-art, YAGNI and progressive disclosure;
- selective/JIT technical contracts;
- authorization boundaries;
- implementation actionability;
- over-specification/premature detail risks.

Distinguish:
1. material defect requiring strategic plan revision;
2. bounded Execution Prep/JIT concern;
3. optional improvement/presentation preference.

Do not issue a negative finding merely because another valid decomposition is possible.

## Verdict

Use:
- `GREEN` — strategically sufficient for Execution Prep under frozen Definition;
- `RED` — material strategic defect requires plan revision before Execution Prep.

For every material finding include:
- severity;
- exact plan section;
- authority implicated;
- concrete failure/rework/safety consequence;
- smallest appropriate correction;
- classification: strategic-plan revision vs Execution Prep/JIT.

For GREEN, include residual risks and strongest challenge findings even when they do not require revision.

## Allowed write

Update exactly this file only.

Change:
- `Status: pending` -> `Status: in_progress` when review begins;
- then -> `Status: green` or `Status: red` with full evidence/report.

No other repository write is allowed.

## Completion boundary

After final verdict/evidence is written:
- reread this file;
- verify subject blob remains `0d55b03e2a4d1a2b1a4fd9972f8365f693262503`;
- STOP.

Do not correct the plan.
Do not enter Execution Prep.
Do not perform meta-synthesis.
Do not touch canonical `planning/reviews/PWV2-P1.md`.

---

## Wynik niezależnego strategic review — 2026-09-22

**Verdict: GREEN.** Dokładny zamrożony plan jest strategicznie wystarczający do Execution Prep względem zamrożonej Definition R1. Nie stwierdzono materialnego defektu strategicznego, kompletnościowego ani correctness wymagającego rewizji planu przed tym etapem. Liczba materialnych findingów: **0**; w szczególności nie wykazano otwartego defektu P0/P1.

To werdykt tego eksperymentu. Nie stanowi zatwierdzenia canonical Plan Review, dowodu implementacji ani wyniku testów V2. Nie uruchamia Execution Prep, adopcji, migracji ani zmiany kontrolera. Pokrycie ocenione poniżej oznacza dostatecznie określoną strategię implementacji i odbioru, nie wykonany PASS.

Decydujące podstawy GREEN:

- Wszystkie 76 wymagań mają rzeczywistą realizację w treści pakietów, właściciela i warunek odbioru. Appendix A nie zastępuje tych opisów.
- Wszystkie 97 pozycji salvage zachowuje dokładnie źródło i disposition z frozen matrix. Każda ma implementacyjny albo świadomie niekodowy rezultat. Osobno zachowano 20 standalone DROP assertions oraz zakaz zwykłego `returned` z R1.
- Plan rozdziela jeden aktywny Card od wewnętrznej współbieżności runtime; obowiązek delegowania od samej dostępności wykonania; semantyczną niezależność review od tożsamości modelu; Stage-6 od Stage-9.
- Ryzyka nieodwracalnego błędu mają konkretne miejsce w strategii: readback przed retry, zachowanie dowodów przed usunięciem źródła, refresh przed reuse review, materialna zmiana → nowy subject, jedna aktywna custody i ograniczony rollback.
- Empiryczne założenia platformy nie są przedstawione jako spełnione. Wczesny M01.P3 poprzedza pełną budowę, a rzeczywiste L01–L09 pozostają warunkiem pierwszego odbioru produkcyjnego.

### 1. Odtworzony kontrakt i pochodzenie dowodów

Nadrzędny kontrakt eksperymentu to początkowe sekcje tego recordu, odczytane przed planem. Reviewer surface: **Codex / Astra Max**, rola: experimental independent reviewer. Nie wybrano canonical execution policy. Odwołania planu do V1 `chatgpt_only` opisują historyczną kontrolę jego budowy; nie określają uprawnień tego review.

**Subject:** [planning/PROJECT_WORKFLOW_V2_MASTER_PLAN.md](https://github.com/elmakus/chatgpt-codex-project-workflow/blob/4b8d2eefa04ea7511edd92e1799e0fd641f57428/planning/PROJECT_WORKFLOW_V2_MASTER_PLAN.md), commit `4b8d2eefa04ea7511edd92e1799e0fd641f57428`, blob **`0d55b03e2a4d1a2b1a4fd9972f8365f693262503`**; 564 linie, 85 871 bajtów. Odczytano cały blob, nie ruchomy branch-tip. Notacja **P:Lx–Ly** poniżej oznacza linie tego dokładnego pliku w tym commicie; nazwy sekcji/pakietów również odnoszą się do tego subjectu.

**Frozen authority:** commit **`8055ed00acdb708c79919d470217fd87c920973a`**. Wszystkie poniższe pliki przeczytano w całości:

| Dokument | Blob frozen authority |
|---|---|
| `requirements/PROJECT_WORKFLOW_V2.md` — R1, REQ-001..076, constraints, non-goals, invariants, acceptance | `74dfc146e095f1e64e0184bfe1b5205c92880daa` |
| `decisions/ADR_PROJECT_WORKFLOW_V2_SINGLE_SEMANTIC_CORE.md` — ADR-001 | `9c6da3b96a8a58f9548c7098ac3ac7b22fa383ba` |
| `decisions/ADR_PROJECT_WORKFLOW_V2_DELIVERY_BOOTSTRAP.md` — ADR-002 | `80c6834859064a9bf14d98d3ba15837923f14c5d` |
| `decisions/ADR_PROJECT_WORKFLOW_V2_MANAGED_CHANGE_LIFECYCLE.md` — ADR-003 | `8b411b761a1d72f1ea7fc74ff05819f25b08d9f2` |
| `decisions/ADR_PROJECT_WORKFLOW_V2_EXECUTION_BOUNDARY.md` — ADR-004 | `bf185e133ecd86db5b79d50d36ee40f363567897` |
| `decisions/ADR_PROJECT_WORKFLOW_V2_REVIEW_AND_PREMIUM_PLANNING.md` — ADR-005 | `4ec9542246ed897b5535bcff57da8ed656448a8f` |
| `decisions/ADR_PROJECT_WORKFLOW_V2_CONTEXT_RESEARCH_YAGNI.md` — ADR-006 | `27b0441890d31caae117ba898458208bb5b7ba4e` |
| `brainstorming/V1_TO_V2_COVERAGE_MATRIX.md` | `aafd4a916ae11f8a3ff0c6edb799d8ced996a4bf` |
| `brainstorming/V2_VALIDATION_MATRIX.md` | `8ea845e85c857235a2fc0a559c983faef1a2b002` |
| `implementation/workstreams/feature-common-preexecution-core/handoffs/DEFINITION_COMPLETE_2026-09-22.md` | `8750c634caee0152e75eab2d9c3e8d1f94549058` |

Pomocniczo sprawdzono wyłącznie historyczne wejścia jawnie wskazane przez plan, aby zweryfikować zachowany oracle i zakres salvage:

- przy tym samym frozen checkpoint: `brainstorming/live-tests/ORCHESTRATION_TOPOLOGY_N_AUTHORITY.md` (`dda4a28bbd0104ffbb463913138aba13462331b8`), `ORCHESTRATION_TOPOLOGY_N_CAPABLE.md` (`944fb86656663e3ef083409442fca2b202b8c36f`) i `ORCHESTRATION_TOPOLOGY_N_CHATGPT.md` (`7d812b023f9b610f04550439d0759ba53433711b`);
- `workflow/common/FORK_RELEASE_VERSIONING.md` przy wskazanym przez plan V1 commit `7aa7512ead67a86256089d1af0171e2e655e700d`, blob `b8a4d9f23ba93957d0daa9c7093145db0256a871`.

Te wejścia służą sprawdzeniu semantycznego salvage, nie nadaniu starym harnessom albo V1 route nadrzędności nad Definition. Nie uruchamiano ich. Zewnętrzne źródła cytowane w §2.1 planu nie zostały potraktowane jako aktualny dowód poprawnego działania platformy; plan sam wymaga nowego empirycznego sprawdzenia M01/M05. Review nie potrzebuje uznania tych historycznych obserwacji za dzisiejsze gwarancje.

**Independence/blindness:** ten kontekst nie tworzył ani nie naprawiał reviewed subjectu. Nie czytano planu ChatGPT, blind A/B judge report, reveal, ChatGPT review, późniejszego canonical verdict, materiałów porównujących modele ani planner-side audit. Nie oceniano jakości na podstawie wspólnej rodziny modelu. Wynik powstał z treści subjectu i powyższych zamrożonych wejść.

**Write-space:** wyłącznie niniejszy record na `exp/v2-plan-astra-max-review`. Status zmieniono z `pending` na `in_progress` przed merytorycznym review. Plan, canonical `planning/reviews/PWV2-P1.md`, canonical workstream i `elmakus/project_workflow_v2` pozostają poza zakresem zapisu. Zakończenie: zapis verdict/evidence → ponowny odczyt recordu → potwierdzenie bloba subjectu → STOP.

### 2. Metoda i kontrole kompletności

Przeprowadzono odczyt pełnych dokumentów, porównanie znaczenia wymagań z pakietami/odbiorami oraz analizę sekwencji awarii i powrotu do pracy. Dodatkowo wykonano mechaniczne sprawdzenie tabel i hasha:

| Kontrola strukturalna | Wynik |
|---|---|
| Git blob obliczony z odczytanych bajtów oraz powiązanie subject commit:path | `0d55b03e2a4d1a2b1a4fd9972f8365f693262503` |
| REQ w frozen authority i Appendix A | 76/76, dokładnie 001..076, bez luk/duplikatów |
| Źródło + disposition frozen matrix vs Appendix B | 97/97 zgodnych par w kolejności, 0 różnic |
| S-identyfikatory oraz destination/assertion | S001..S097, wszystkie z niepustym rezultatem |
| Automatyczne scenariusze | A01..A17, 17/17 w §6.1 |
| Rzeczywiste scenariusze | L01..L09, 9/9 w §6.2 |
| Standalone explicit drops | 20; zbadane osobno od 97 wierszy |
| Wiersze z DROP lub częściowym DROP | 23; wszystkie zachowują negatywny zakres |

Te kontrole nie dowodzą correctness. Znaczenie każdego wiersza sprawdzono wobec treści planu; wynik szczegółowy jest w sekcjach 5–8 tego raportu. Nie uruchamiano implementacyjnych A/L i nie oznaczono ich jako wykonane GREEN.

### 3. Najsilniejsze challenge findings i ograniczone concerns

**Material strategic defects: brak.** Poniższe pozycje mają klasyfikację **Execution Prep/JIT**, nie strategic-plan revision. Ich priorytet oznacza ryzyko realizacji, a nie wykryty defekt istniejącej implementacji. Nie są dodatkowymi warunkami uzyskania GREEN przez ten plan; konkretyzują pracę już nakazaną jego pakietami i testami.

#### J01 — Moment przekazania custody i powrót po częściowym cutover

- **Severity:** P2, podwyższone ryzyko realizacji; błędna realizacja może spowodować poważną utratę kontroli nad stanem.
- **Plan:** §4, P:L149–157; M06.P3/P4, L264–267; M07.P4, L282; §8 cutover/rollback, L363–367.
- **Authority:** REQ-017/018/031–033/064/072; ADR-001/003; constraints o V1 development/history authority.
- **Challenge/consequence:** po zapisaniu terminalnego transferu w V1, ale przed uruchomieniem bootstrapu V2, samo przywrócenie starej instalacji nie musi przywracać prawa V1 do mutacji. Niejasne znaczenie „activation” może prowadzić do dwóch właścicieli albo skasowania jedynego staged recovery package.
- **Dlaczego nie RED:** plan już nakazuje jednego właściciela, weryfikację destination przed transferem, brak dual-write, zatrzymanie mutacji przy niepewności i test custody interruption. Nie zakłada atomowości dwóch repozytoriów. Strategia nie wymaga odwracania już wykonanych efektów przez reinstalację.
- **Najmniejsze właściwe doprecyzowanie:** w kontrakcie transferu M06/M07 wybrać jednoznaczny punkt przejęcia authority i tabelę odzyskiwania dla: przed staging, po staging, po retirement V1, przed/po włączeniu delivery i po pierwszym nowym efekcie V2. Oddzielić aktywację właściciela od aktywacji instalacji; odtworzenie V1 authority wymaga durable reconciliation. Bez nowego globalnego rejestru lub rozproszonego koordynatora.
- **Klasyfikacja:** Execution Prep/JIT.

#### J02 — Dokładna wykonalność pluginu, nazwy Skill i izolacji instalacji

- **Severity:** P2, ryzyko dostępności/platformy.
- **Plan:** §2.1, L49–59; M01.P3, L177–182; M05.P2/P3, L244–252.
- **Authority:** REQ-007–014; ADR-002/006; L04/L05.
- **Challenge/consequence:** dokumentacja lub poprawny manifest nie dowodzą, że zainstalowany host odkryje `$pw:project_workflow_v2`, właściwy root i SessionStart. Konflikt dwóch źródeł `pw` lub cache może dać pozorny PASS na kodzie V1 albo starym pakiecie.
- **Dlaczego nie RED:** pierwszy rzeczywisty probe jest warunkiem M01, przed pełną budową; błędna nazwa nie może zostać cicho zastąpiona. M05 osobno wymaga aktualizacji, świeżej sesji, readback bajtów i identyfikacji źródła. Nie ma założenia, że V1 evidence wystarczy.
- **Najmniejsze właściwe doprecyzowanie:** określić izolowane środowisko i jego uprawnienia przed probe; zachować dowód dokładnej invocation, źródła pakietu, root, trust i zachowania przy braku routera. Odróżnić wczesny feasibility result od pełnego L04/L05. Jeśli host uniemożliwia warunek Definition, zastosować już opisany Research/Definition route.
- **Klasyfikacja:** Execution Prep/JIT.

#### J03 — Testy kontraktu muszą badać używaną semantykę

- **Severity:** P2, ryzyko fałszywej pewności walidacji.
- **Plan:** M01.P4, L178–182; §6, L290–292; M07.P1, L279; §6.2, L332–334.
- **Authority:** REQ-013–015/074–076; ADR-006; A01/A02/A17 oraz L01–L09.
- **Challenge/consequence:** napisany osobno testowy router może przechodzić wszystkie scenariusze, podczas gdy agent czyta sprzeczne Markdown. Liczba słów kluczowych lub kompletność tabel nie wykryje takiej rozbieżności.
- **Dlaczego nie RED:** plan zakazuje test-only interpretera niezwiązanego z produkcją i testów opartych wyłącznie na substringach; wymaga rzeczywistych parserów, wspólnych uzasadnionych constraints, scenariuszy, review i live traces.
- **Najmniejsze właściwe doprecyzowanie:** każdy test powiązać z rzeczywistym modułem/fixture/helperem, określić oracle i wykazać, że przeciwna semantyka powoduje failure. Nie rozbudowywać tego w nowy execution engine. Zachować odrębne dowody zachowania rzeczywistych powierzchni.
- **Klasyfikacja:** Execution Prep/JIT.

#### J04 — Tożsamość subjectu, final-review reuse i wyścig targetu

- **Severity:** P2, ryzyko implementacji ważnego warunku bezpieczeństwa.
- **Plan:** §3.1, L123–128; M03.P3, L211; M04.P1, L226; §6.1 A08/A09, L305–306; §8, L362.
- **Authority:** REQ-034–038/061–063; ADR-005; A07–A09.
- **Challenge/consequence:** sam hash pojedynczego pliku może nie pokrywać zależności i acceptance; hash całego commita może natomiast zmieniać się od samego dopisania review evidence. Target może przesunąć się ponownie między refresh a merge. To grozi reuse nieaktualnego GREEN albo nieskończoną pętlą re-review.
- **Dlaczego nie RED:** plan wiąże subject z content **i** acceptance, wymaga kompatybilności po refresh, odrzuca clean-merge-only proof, wymaga nowego subjectu przy materialnej zmianie i osobnego aktualnego odczytu przed mutacją. Nie ustanawia commit SHA jedynym kryterium.
- **Najmniejsze właściwe doprecyzowanie:** w M03/M04 wybrać reprezentację content/acceptance i zakres neutralnego bookkeeping; ustalić regułę reuse oraz sposób wykrywania/odrzucania ponownego ruchu targetu dla konkretnej metody integracji. Testować ruch przed freeze, po review i tuż przed mutacją. Nie dodawać obowiązkowego re-review dla każdej zmiany SHA.
- **Klasyfikacja:** Execution Prep/JIT.

#### J05 — Trwałość referencji po merge, squash i złożeniu workstreamów

- **Severity:** P2, ryzyko terminal recovery.
- **Plan:** §3.1 terminal package, L126; M04.P3, L228–231; §6.1 A10, L307.
- **Authority:** REQ-018/020/064/065; salvage S022/S034/S035/S057.
- **Challenge/consequence:** locator do usuniętej gałęzi, nieosiągalnego commita albo tylko parent branch może wyglądać poprawnie przed merge i nie odtworzyć unikalnej authority/review/evidence po cleanup. Sam sukces merge nie dowodzi zachowania pełnego pakietu.
- **Dlaczego nie RED:** plan każe umieścić wszystkie unikalne znane artefakty w merge subject przed merge, odzyskiwać późniejszy wynik z targetu i immutable merge evidence oraz sprawdzać niezależną rozwiązywalność refs. Obejmuje oba stacked paths i unmerged terminal closure.
- **Najmniejsze właściwe doprecyzowanie:** ustalić, które artefakty są kopiowane, a które mają trwałą osiągalną referencję; fixtures dobrać do wspieranych merge methods. Sprawdzić source i parent disappearance oraz trwałość rejected-work recovery bez importu odrzuconej implementacji.
- **Klasyfikacja:** Execution Prep/JIT.

#### J06 — Migracja nie może zgadywać zgody, niezależności ani wyniku efektu

- **Severity:** P2, ryzyko utraty semantyki podczas konwersji.
- **Plan:** M06.P1–P4, L262–269; §8 rollback, L367.
- **Authority:** REQ-031–037/040–045/053–055/072; A05/A06/A07/A15.
- **Challenge/consequence:** usunięcie starego pola runtime/scheduler może przypadkiem usunąć dowód disqualification review albo niezakończonej operacji. Stary GREEN lub marker issue nie stanowi dowodu zaakceptowanej naprawy. Dry run może się zdezaktualizować przed apply.
- **Dlaczego nie RED:** plan explicite zachowuje obowiązki semantyczne, blokuje nieznany/niejednoznaczny input, wymaga quiescence pod V1 i dokładnej tożsamości źródła; brak dowodu tworzy obowiązek, nie fikcyjny PASS. Idempotency i crash points są częścią odbioru.
- **Najmniejsze właściwe doprecyzowanie:** wybrać rzeczywiste wspierane warianty i tabelę transformacji, w tym brakujące zgody, historyczne RED/GREEN, pending effects i źródło zmienione po dry run. Rozróżnić identyczny repeat od konfliktu destination. Przed aktywacją przećwiczyć powrót; po nowych efektach stosować opisane hold/readback/forward correction.
- **Klasyfikacja:** Execution Prep/JIT.

#### J07 — Jedna Card i jeden reconciler wymagają kontroli stale writes

- **Severity:** P2, ryzyko spójności przy recovery/delegacji.
- **Plan:** §3.1, L121–128; §3.2, L135–139; M03.P1/P2/P4, L209–214; M04.P2, L227.
- **Authority:** REQ-021–027/030–033; ADR-004; A03–A06.
- **Challenge/consequence:** sprawdzenie liczby aktywnych Cards nie wystarcza, jeśli stary wynik lub wznowiony koordynator nadpisze nowszy board; read-before-create bez dokładnej korelacji nie gwarantuje dedup niepewnego efektu.
- **Dlaczego nie RED:** plan już ustanawia Main jedynym writerem, launch refresh, exact result checks, reconciliation zamiast replay i fail-closed niepewności. Runtime workers nie mogą samodzielnie finalizować stanu. Nie obiecuje wielokoordynatorowego scheduler service.
- **Najmniejsze właściwe doprecyzowanie:** wybrać minimalną kontrolę aktualności rewizji/expected state w używanym Git/API i test odrzucenia stale result/write, w tym recovery po utracie runtime. Korelację efektu trzymać przy jego obowiązku. Nie przywracać `active_execution`, globalnego lock registry ani canonical worker/session IDs.
- **Klasyfikacja:** Execution Prep/JIT.

#### J08 — Odzyskiwanie premium gates i materialny RED replan

- **Severity:** P2, ryzyko nieprawidłowego przejścia między rolami.
- **Plan:** §1, L37; §3.2, L136–143; M02.P3, L194–197; M07.P2/P3, L280–286.
- **Authority:** REQ-039–045/067–071; ADR-005; L07–L09.
- **Challenge/consequence:** ogólne „RED nie jest stopem” może zostać błędnie zastosowane do materialnego replan, albo każda świeża sesja może bez końca odsyłać do kolejnej. Z kolei sam dowolny user reply nie może legalizować issue repair.
- **Dlaczego nie RED:** plan ma jawny Stage-6 exception, powtarzanie A/B/C dla materialnego replan, dokładne authorized entry/response i osobne oracles Stage-9. M02.P1 explicite odrzuca safety-question jako zgodę. Nie ma sprzeczności wymagającej nowej strategii.
- **Najmniejsze właściwe doprecyzowanie:** tabela przejść powinna rozróżniać aktywny stop, legalne wejście po nim, editorial correction, materialny replan i Stage-9 bounded repair; przetestować recovery po każdym zapisie. Stage-9 GREEN finalizuje, Stage-6 GREEN prowadzi do C. Dowód nie wymaga canonical model/session IDs.
- **Klasyfikacja:** Execution Prep/JIT.

### 4. Zależności, założenia P0/P1 i actionability

M01 → M02 → M03 → M04 → M05 → M06 → M07 jest wykonalnym porządkiem. M01 ustanawia minimum stanu/routera i rzeczywisty probe; M02 dostarcza authority, human gates i tracker opening; M03 wykonanie/review; M04 bezpieczne final integration; M05 pełne delivery i L01–L05; M06 ćwiczy migrację na stabilnych semantykach; M07 kwalifikuje system i scoped adoption. M06 może wcześniej badać wejścia, lecz jego odbiór wymaga dojrzałych transitions i delivery do rehearsal. To nie autoryzuje równoległych Project Cards (P:L163–165, L258).

Nie ma cyklu „V2 musi kontrolować własną budowę, zanim istnieje”. V1 jest jedynym construction trackerem; Cards mają zewnętrzne dokładne V2 subjects, nie podmieniony V1 manifest/board binding. Dopiero M07 przenosi authority. Wyjątek dwóch repozytoriów jest ograniczony do self-hosting construction, uzasadniony §4 i zgodny z frozen constraints. Nie trafia do zwykłego modelu projektu V2.

| Hipoteza mogąca powodować P0/P1 | Kontrdowód / granica w dokładnym planie | Ocena |
|---|---|---|
| Pusta nazwana target repo będzie nadal pusta podczas inicjalizacji | §2 L42 i §4 L154 wymagają świeżego readback; populated target nie może być nadpisany | Brak fałszywego założenia |
| Zapis V1 control commit oznacza dostarczenie V2 | §4 L151–155 wymaga dokładnego V2 branch/commit i readback obu repo | Odrzucone |
| Bezpośredni zapis produktu na default branch jest potrzebny do bootstrapu | §4 L154 ogranicza wyjątek do no-content initialization; produkt dopiero na branch/PR | Ograniczony konieczny wyjątek, nie furtka |
| Stary plugin lub dokumentacja dowodzi V2 invocation/update | §2 L43/59, M01.P3 i M05.P2/P3 rozdzielają prior art od empirycznego proof | Kontrolowane przez J02 |
| GREEN można odzyskać tylko z nazwy modelu lub starego verdict | §3.1 L123/128 i M03.P3/P4 wymagają subject/acceptance i semantic independence | Odrzucone; kodowanie JIT |
| Każda zmiana SHA wymaga review, a clean merge dowodzi kompatybilności | M04.P1 jawnie odrzuca obie reguły | Poprawne rozróżnienie |
| Branch będzie żył do końca Close | M04.P3/A10 wymagają dowodów przed merge i source-independent recovery | Odrzucone |
| Dwa repozytoria/instalacja/efekt dają się cofnąć atomowo | §4 L155–157, M06.P3 i §8 L367 przeczą temu | Kontrolowane przez J01/J06 |
| Automat dowodzi realnego zachowania ChatGPT/Codex | §6 L290–292/334 oraz M07 wymagają osobnych live proofs | Odrzucone |
| N-CAPABLE jest zawsze dostępne lub można zastąpić je symulatorem | M07 L284–286 pozostawia test blocked; brak waiver pierwszej produkcji | Ryzyko dostępności, nie ukryta przesłanka correctness |
| „One Card” zabrania równoległych subagentów albo usprawiedliwia niedelegowanie | M03.P2 nakazuje delegację przy kwalifikującej zdolności, dopuszcza concurrency wewnątrz Card | Zgodne z ADR-004 |
| Deployment albo sam `#issue` przesądza o zgodzie/stopie | M02.P1 i M04.P4 stosują przyjęte boundaries zamiast etykiety operacji | Zgodne z human control |
| Czasowe rozdzielenie wersji pluginu i GitHub wymaga execution_policy lub per-project patch pin | M05 L252 przewiduje update/readback i fail-closed niekompatybilności bez takich konstrukcji | Dopuszczalna strategia; compatibility representation JIT |

**Actionability:** każdy milestone ma outcome, dependencies, konkretne P1–P4, checkpoint, acceptance i ograniczenie JIT. Execution Prep może z tego utworzyć użyteczne bounded Cards bez zgadywania architektury lub nowej decyzji produktowej. Szczegółowe algorytmy konwersji, serializacja, operation syntax, reprezentacja review subjectu i konkretny cutoff transferu mogą powstać tuż przed odpowiednimi pracami. Ich brak w Master Planie nie jest luką strategiczną.

**Over-specification/YAGNI:** layout jest jawnie punktem startowym, a nie zamrożoną pełną API; rozszerzenia schema powstają u właścicieli, optional templates i OpenSpec mają warunek wartości, fork module ma rzeczywisty trigger. Duże appendices wynikają z audytowalnego zakresu 76/97, nie z wymogu ładowania ich w każdym runtime entry. Szczegóły lineage M04.P4 są zgodne z jawnie salvaged V1 contract i nie zmieniają V2 w fork ani system publikacji. Nie ma uzasadnienia do RED za inną poprawną dekompozycję siedmiu milestones.

**Opcjonalne ulepszenia (P3; preferencja organizacyjna, bez strategic-plan revision):** można wcześniej sprawdzić dostępność rzeczywistych powierzchni L08/L09, aby ograniczyć ryzyko późnego oczekiwania; można prezentować wynik odbioru w krótszym indeksie z dokładnymi refs, zachowując pełne evidence. Nie dodaje to nowych gate, frameworków, osobnego control repo ani manualnych testów ponad zaakceptowany zakres.

### 5. Pełny audyt PWV2-REQ-001..076

Wynik każdego wiersza: **COVERED na poziomie strategicznym**. Kolumna oceny opisuje sprawdzoną treść pakietów, nie tylko obecność identyfikatora. Authority dla REQ-n to frozen R1, linia 20+n. Odnośnik `Appendix A L...` identyfikuje dodatkowo dokładny wiersz traceability planu.

| Wymaganie | Dokładny obszar planu | Niezależna ocena pokrycia / warunek zachowania semantyki |
|---|---|---|
| PWV2-REQ-001 | §3; M01.P1/P2; Appendix A L377 | Jedno canonical workflow; layout i testy A01/A02/A17 egzekwują granicę, nie tylko deklarują nazwę. |
| PWV2-REQ-002 | §3; M01.P4; M06; Appendix A L378 | Brak production policy trees; historyczne wejścia migracji są wyraźnie odseparowane od normal route. |
| PWV2-REQ-003 | §3.1; M01.P4; M06.P2; Appendix A L379 | Nowe state nie wybiera execution_policy; stary selector jest wyłącznie inputem konwersji. |
| PWV2-REQ-004 | §3.1; §6.2; Appendix A L380 | Rozdzielono canonical state od obserwacji platformy w test evidence; L06 nie wymaga przepisywania identity. |
| PWV2-REQ-005 | M07.P2; M05 końcowy akapit; Appendix A L381 | L06 sprawdza obie zmiany runtime na tym samym workstream; update lag nie legalizuje konwersji stanu. |
| PWV2-REQ-006 | §3.1; M03.P2; Appendix A L382 | Właściciele semantic state są jawni; topology nie staje się kontraktem produktu. A04/L08 sprawdzają rozdział. |
| PWV2-REQ-007 | M05.P1; §6.2 L01; Appendix A L383 | User-owned Project Instructions prowadzą do V2 GitHub; consumer state pozostaje w repo projektu. |
| PWV2-REQ-008 | M05.P2; §6.2 L04; Appendix A L384 | Zwykłe Codex policy acquisition jest lokalne; missing authority nie uruchamia remote fallback. |
| PWV2-REQ-009 | M01.P3; M05.P2; Appendix A L385 | Dokładna nazwa/invocation ma wczesny empiryczny gate i końcowe L04. Nie oparto jej na V1 PASS. |
| PWV2-REQ-010 | §3; M05.P2/P3; Appendix A L386 | Jeden editable tree; dopuszczalny package artifact jest byte-preserving, nie drugą kopią semantyczną. |
| PWV2-REQ-011 | M05.P3; L05; Appendix A L387 | Test zmienia wyłącznie canonical module i sprawdza niezmienione bootstrap hashes oraz rzeczywisty update. |
| PWV2-REQ-012 | §3; M05; §8; Appendix A L388 | Provisioning i pinning pozostają przy newproject-skill; V2 definiuje delivery contract, nie nowy provisioner. |
| PWV2-REQ-013 | §3.2; M01.P4; M05; Appendix A L389 | Router dobiera konkretny obowiązek przed pełnym module read; read-set fixtures są uzupełnione live traces. |
| PWV2-REQ-014 | §3.2; M05.P1/P2; Appendix A L390 | Thin entry nie musi czytać całego drzewa/templates/history. Odbiór obejmuje rzeczywiste loading behavior. |
| PWV2-REQ-015 | §3.1/3.2; M01.P2; Appendix A L391 | Dokładne authority/evidence refs mają walidację binding/class/path; broad scan nie jest normalnym recovery. |
| PWV2-REQ-016 | §3.1; M01.P2; Appendix A L392 | Common V2 marker identyfikuje kontrakt, nie current runtime lub installed path. A02/A03 obejmują templates. |
| PWV2-REQ-017 | §4; M01.P1; M07.P4; Appendix A L393 | Consumer single-repo zachowany; konstrukcyjny wyjątek ma uzasadnienie, jednego ownera i terminal transfer. J01. |
| PWV2-REQ-018 | §4; M01.P1/P2; M02.P1; Appendix A L394 | Branch/manifest powstają przed change-specific writes; oddzielono V1 control binding od V2 delivery subject. |
| PWV2-REQ-019 | §3; M01.P4; Appendix A L395 | Correctness opiera się na exact workstream, nie mutable global index; negatywne A02/A03/A17. |
| PWV2-REQ-020 | §3.1; M04.P3; Appendix A L396 | Rzeczywista parent-only dependency i provenance; oba legalne sposoby integracji oraz parent disappearance. J05. |
| PWV2-REQ-021 | §3.1; M03.P1/P2; Appendix A L397 | Card ma stabilny scope/tests; board posiada mutable results/reviews. Nie powstają konkurujące mirrors. |
| PWV2-REQ-022 | M03.P2; A04; Appendix A L398 | Jedna executing Card w wybranym workstream. Nie rozciągnięto zakazu na wewnętrzną pracę runtime. |
| PWV2-REQ-023 | §3/3.1; M01.P4; M06; Appendix A L399 | Zakaz scheduler/wrappers obejmuje zwykłe returned; fixtures historyczne nie stają się dozwolonym V2 outputem. |
| PWV2-REQ-024 | M03.P2; A04/L08; Appendix A L400 | Zero/jeden/wiele workers może realizować jedną Card; shared board/manifest pozostają poza ich write-space. |
| PWV2-REQ-025 | M03.P2; M07.P3; Appendix A L401 | Delegowanie jest obowiązkiem przy kwalifikującej zdolności; sama wygoda Main nie jest wyjątkiem. |
| PWV2-REQ-026 | M03.P2/P4; A05; Appendix A L402 | Worker zwraca evidence; Main waliduje i finalizuje. Wynik worker nie jest samoistną zmianą project truth. |
| PWV2-REQ-027 | M03.P2; L06/L09; Appendix A L403 | Genuine brak delegation pozwala na direct execution bez innego policy/state. Nie zmienia review independence. |
| PWV2-REQ-028 | M03.P1; Appendix A L404 | Prep materializuje wszystkie użyteczne znane Cards; nie tylko pierwszą, ani speculative placeholders. |
| PWV2-REQ-029 | M03.P1; §7; Appendix A L405 | Refinement unstarted Cards pozostaje wewnątrz authority; strategy/intent mają oddzielne escalation destinations. |
| PWV2-REQ-030 | M03.P1/P2; Appendix A L406 | READY oznacza legalność, nie dostępność worker; launch refresh rereads result/authority/dependencies. J07. |
| PWV2-REQ-031 | §3.2; M03.P4; M06; Appendix A L407 | Completed result wraca do reconciliation, nie replay. A05/L06 i migracja chronią recovery bez runtime IDs. |
| PWV2-REQ-032 | M04.P2; A06; M06.P3; Appendix A L408 | Unknown occurrence → exact readback przed retry; nierozstrzygnięta operacja nie jest automatycznie powtarzana. |
| PWV2-REQ-033 | §3.1; M02.P4; M04.P2; Appendix A L409 | Write/readback/expected-state/evidence dotyczy również Issue opening, nie tylko końcowego merge. |
| PWV2-REQ-034 | §3.1; M03.P3; Appendix A L410 | Immutable content i acceptance, append-only attempts dla zmienionego subject/verdict; RED nie jest nadpisywane. |
| PWV2-REQ-035 | M03.P3; L08/L09; Appendix A L411 | Material producer/repairer jest disqualified dla danego subjectu; nowy subject wymaga nowej oceny independence. |
| PWV2-REQ-036 | M03.P3; A07; Appendix A L412 | REQUIRED i activated RECOMMENDED blokują do GREEN; ryzyko/frequency nie daje waiver aktywnego gate. |
| PWV2-REQ-037 | §3.1; M03.P3/P4; Appendix A L413 | Semantic proof jest obowiązkowy mimo wykluczenia telemetry. Brak identity nie usprawiedliwia braku dowodu. |
| PWV2-REQ-038 | M03.P3; M04.P1; M07.P1; Appendix A L414 | Normal behavior final review obowiązkowe; wyjątek wymaga pełnego exact coverage po refresh, nie ogólnego dawnego GREEN. |
| PWV2-REQ-039 | M02.P3; §1; Appendix A L415 | Nowy/material plan zawsze review; editorial exception ograniczone do niematerialnych zmian strategii/coverage/gates. |
| PWV2-REQ-040 | §3.2; M02.P3; L07; Appendix A L416 | A jest trwałym stopem po Definition, nie rekomendacją pomijaną przez automatyczny router. |
| PWV2-REQ-041 | M02.P3; M07.P2; Appendix A L417 | Best available model/context to human-facing recommendation; brak hard-coded product/model w canonical policy. |
| PWV2-REQ-042 | M02.P3; L07; Appendix A L418 | Freeze poprzedza B; planner internal spawn wykluczony mimo capability-first reguł Stage-9. |
| PWV2-REQ-043 | M02.P3; §1; L07; Appendix A L419 | Approval GREEN nie przechodzi do Prep; zapis C i rekomendacja lżejszego kontekstu mają osobny obowiązek. |
| PWV2-REQ-044 | §1; M02.P3; §7; Appendix A L420 | Materialny replan powtarza A/B/C; nie jest L2 refinement. J08 dotyczy zakodowania cases, nie braku zasady. |
| PWV2-REQ-045 | M02.P1/P3; M03.P1; Appendix A L421 | Micro-fix może ominąć full plan, ale dopiero po alignment i ze scope/tests/review; brak auto-repair shortcut. |
| PWV2-REQ-046 | M02.P2; A17/L01; Appendix A L422 | Grilling jest intrinsic; stare #grill może wystąpić jako historyczny tekst, nie aktywny command. |
| PWV2-REQ-047 | M02.P2; L01; Appendix A L423 | Pytania materialne, tematyczne/numerowane, z rekomendacją; stopping criterion opiera się na wartości kolejnej rundy. |
| PWV2-REQ-048 | M02.P2; A13/L01; Appendix A L424 | Agent prowadzi factual research, kończy challenge audit; obowiązek nie jest przerzucony na użytkownika. |
| PWV2-REQ-049 | M02.P2; A13; §2.1; Appendix A L425 | Wymagany proporcjonalny prior-art obejmuje official/upstream, project/runtime i issue/community; bez official-only skrótu. |
| PWV2-REQ-050 | M02.P2; A13; Appendix A L426 | Źródła mają weight/conflict/limits; popularność nie nadaje authority ani prawa do zmiany scope. |
| PWV2-REQ-051 | §3; M03.P1; A12; Appendix A L427 | Brak zbędnego daemon/DB/DAG; jednocześnie YAGNI nie usuwa correctness, security, migration i observability. |
| PWV2-REQ-052 | M03.P1; A11; Appendix A L428 | Każda zmiana ma precyzyjny Card; dodatkowy technical contract wyzwala materialna wartość, nie rozmiar ceremonii. |
| PWV2-REQ-053 | M02.P1; L02; Appendix A L429 | Marker issue autoryzuje intake/diagnosis, nie implementację; tracker bookkeeping nie jest zgodą na naprawę. |
| PWV2-REQ-054 | M02.P1; M02 acceptance; Appendix A L430 | Diagnosis/outcome/safety/recommendation poprzedzają późniejszą aligned response; pytanie o bezpieczeństwo nie wystarcza. |
| PWV2-REQ-055 | M02.P1/P2; L02; Appendix A L431 | Zmiana outcome/concern uruchamia dalszą rozmowę i unieważnia stale alignment; nie ma automatycznego resume fix. |
| PWV2-REQ-056 | M02.P4; A14/L01/L02; Appendix A L432 | Supported tracker jest create/recover po dedup; brak capability uczciwie odnotowany, nie fikcyjny Issue. |
| PWV2-REQ-057 | M02.P4; §3.2; Appendix A L433 | Issue body/status nie zastępuje requirements, state ani user authorization; zewnętrzny tekst nie instruuje routera. |
| PWV2-REQ-058 | §3.1; M02.P4; Appendix A L434 | Repo + Issue + workstream/PR identity pozostają durable; correlation służy recovery, nie drugiemu boardowi. |
| PWV2-REQ-059 | M04.P2; L03; Appendix A L435 | Intermediate PR/commit bez closing linkage; final scope-completing default-branch PR może zamknąć tracker. |
| PWV2-REQ-060 | M04.P2; L03; Appendix A L436 | Readback faktycznego Issue state; explicit close dopiero po durable whole-scope completion, nie po częściowym sukcesie. |
| PWV2-REQ-061 | M04.P1; A09; Appendix A L437 | Refresh → najmniejsza authorized reconciliation → affected tests → coverage decision → aktualny target przed mutation. J04. |
| PWV2-REQ-062 | M04.P1; A08; Appendix A L438 | Ancestry/SHA-only movement nie unieważnia GREEN bez materialnej zmiany; compatibility wciąż musi przejść. |
| PWV2-REQ-063 | M04.P1; A09; Appendix A L439 | Material behavior/content/acceptance change daje nowy frozen subject i independent attempt; nie bookkeeping-only reuse. |
| PWV2-REQ-064 | M04.P3; A10; Appendix A L440 | Unikalne znane evidence przed merge; późny wynik z target/merge evidence bez odtwarzania źródła. J05. |
| PWV2-REQ-065 | M04.P3; cleanup fixtures; Appendix A L441 | Autodelete to normalna realizacja; safe_to_delete dotyczy tylko surviving exact ref, z reread head i absence proof. |
| PWV2-REQ-066 | M04.P2/P4; §8; Appendix A L442 | Deployment nie tworzy stopu samoistnie; osobne istniejące adoption/user-owned configuration gates są zachowane. |
| PWV2-REQ-067 | §3.2; M03.P4; L08/L09; Appendix A L443 | Router kontynuuje deterministic authorized obligations; role change i zwykły verdict nie tworzą nowego stopu. |
| PWV2-REQ-068 | §3.2; M02.P3; Appendix A L444 | Real-stop set obejmuje choice, accepted gates, rzeczywisty blocker, user stop, koniec scope i premium; independence ma legalny resume. |
| PWV2-REQ-069 | §3/3.2; M01.P4; Appendix A L445 | Recovery z durable truth; compaction/session support w hook nie odtwarza Context Health/FRESH lifecycle. |
| PWV2-REQ-070 | M04.P4; §8; Appendix A L446 | True end of accepted scope raportuje completion i kończy; pilot nie uruchamia automatycznie szerszego rollout. |
| PWV2-REQ-071 | §3.2; M05.P1; L07/L09; Appendix A L447 | Locator-only zawiera repo/branch lub legal terminal target/obligation/pointer, nie przepisany plan czy checklistę. |
| PWV2-REQ-072 | M06; §8; Appendix A L448 | Finite supported V1 readers, dry run i jednorazowy apply; history nie jest production semantic route. |
| PWV2-REQ-073 | M04.P4; A16; Appendix A L449 | Fork lineage ładuje się tylko dla declared downstream release; V2 product nie staje się automatycznie forkiem. |
| PWV2-REQ-074 | §6; M07.P1; Appendix A L450 | Deterministyczne kontrakty automatycznie; rzeczywiste surface behavior manualnie. Plan odrzuca fałszywy simulator proof. J03. |
| PWV2-REQ-075 | M07.P3; §8; Appendix A L451 | Oba realne N scenarios obowiązkowe przed produkcją; brak capable topology jest blocked, nie waiver. |
| PWV2-REQ-076 | Appendix B; A17; M07.P1; Appendix A L452 | Wszystkie 97 source/disposition sprawdzone dokładnie; 20 dodatkowych drop assertions i returned mają negatywny odbiór. |

### 6. Fidelity ADR-PWV2-001..006

| ADR | Ocena i konkretna granica sprawdzona w planie |
|---|---|
| ADR-PWV2-001 — single semantic core | COVERED: §3 i M01 określają jeden produkt/runtime-neutral state; M05 zmienia wyłącznie delivery, M06 czyta stare policy jako input. Wyjątek konstrukcyjny §4 nie tworzy nowej policy konsumenta. |
| ADR-PWV2-002 — delivery/bootstrap | COVERED: M01.P3 sprawdza przyjętą nazwę przed pełną realizacją, M05 egzekwuje local bundle i update propagation. Brak patch pin/updater/provisioner w V2; user-owned ChatGPT bootstrap zachowany. |
| ADR-PWV2-003 — managed change | COVERED: §3/4 i M02/M04 łączą branch-first binding, issue alignment, tracker bookkeeping i final-scope closure. Bookkeeping przed zgodą nie staje się implementation authority. |
| ADR-PWV2-004 — execution boundary | COVERED: M03 nie sprowadza „one Card” do „one worker”. Main ma routing/reconciliation, qualifying implementation jest delegowana, a brak capability nie tworzy nowej semantyki. |
| ADR-PWV2-005 — review/premium | COVERED: M03 exact-subject append-only Stage-9 i M02 fresh Stage-6 exception są rozdzielone. A/B/C trwają przez recovery; material replans powtarzają blok. Model identity nie stanowi proof independence. |
| ADR-PWV2-006 — context/Research/YAGNI | COVERED: §3.2 ogranicza read sets; M02 zachowuje source breadth i adaptive grilling; M03/A11/A12 oddziela precyzyjny Card od warunkowego technical contract. Nie ma obligatoryjnego OpenSpec ani official-only Research. |

Definition handoff pozostaje źródłem zakończenia Definition i A; nie uznano jego GREEN za zatwierdzenie planu lub wdrożenia. Plan §1 poprawnie zamraża authority na tym checkpoint, zachowuje przyszłe B/C i nie dziedziczy V1 architecture jako target.

### 7. Pełny audyt 97 pozycji salvage/regression

Każdy wiersz ma wynik **COVERED**: disposition jest wiernie zachowane, a wskazany owner ma dostateczny rezultat/assertion lub explicit non-code disposition. `matrix:L...` to frozen `V1_TO_V2_COVERAGE_MATRIX.md`; `P:L...` to dokładny wiersz Appendix B. Ocena dotyczy zaplanowanego odbioru A17, nie wykonanej regresji.

| ID i dokładne refs | Frozen source / disposition | Właściciel w planie i niezależna ocena |
|---|---|---|
| S001; matrix:L23; P:L460 | `workflow/BRAINSTORMING.md` + fixed-policy Brainstorming copies — **KEEP CORE** | M02.P2. Zachowana jedna semantyka grilling; negatywny test aktywnego #grill obejmuje usunięty operator. |
| S002; matrix:L24; P:L461 | `workflow/common/BRAINSTORMING.md` — **KEEP CORE** | M02.P2. Authority/promotion nie ginie przy połączeniu kopii Brainstorming; final challenge pozostaje. |
| S003; matrix:L25; P:L462 | `workflow/chatgpt_only/INTAKE.md` + `codex_only/INTAKE.md` — **GENERALIZE** | M02.P1/P4. Intake zachowuje managed markers i branch identity; policy routing nie jest kopiowane. |
| S004; matrix:L26; P:L463 | automatic V1 `#issue -> micro_fix` fast path — **DROP** | M02.P1. DROP rzeczywiste: symptom nie uruchamia micro-fix; późniejsza aligned authorization wymagana. |
| S005; matrix:L27; P:L464 | V1 micro-fix contract — **GENERALIZE** | M02.P1 + M03.P1. Proporcjonalna naprawa pozostaje z Card/tests/review; usunięto autonomię, nie użyteczny zakres. |
| S006; matrix:L28; P:L465 | `workflow/RESEARCH.md` + `workflow/common/RESEARCH.md` + fixed-policy Research — **KEEP CORE** | M02.P2. Scalono Research bez utraty source breadth, weighting i dokładnego powrotu do ownera. |
| S007; matrix:L29; P:L466 | `workflow/common/DEFINITION.md` + fixed-policy Definition — **KEEP CORE** | M02.P2. Definition zachowuje explicit user promotion; exploratory zapis nie staje się accepted intent. |
| S008; matrix:L30; P:L467 | `workflow/PLANNING.md` + fixed-policy Planning — **KEEP CORE** | M02.P3. Strategic Planning zachowane z A; nie jest rozproszone do dowolnego execution refinement. |
| S009; matrix:L31; P:L468 | fixed-policy `PLAN_REVIEW.md` — **GENERALIZE** | M02.P3. Świeży niezależny review i B/C zastępują product-specific tożsamość reviewer. |
| S010; matrix:L32; P:L469 | `workflow/EXECUTION_PREP.md` + fixed-policy prep — **GENERALIZE** | M03.P1. JIT i READY zachowane; wykluczono scheduler oraz capability jako warunek samego READY. |
| S011; matrix:L33; P:L470 | root/shared `workflow/EXECUTION.md` + fixed-policy Execution — **GENERALIZE** | M03.P2/P4. Serial Card pozwala na wewnętrzną delegation/concurrency; nie odtworzono drugiej Execution policy. |
| S012; matrix:L34; P:L471 | fixed-policy `REVIEW.md` — **GENERALIZE** | M03.P3. Jedna append-only review lifecycle; stare RED nie jest przepisane na nowe GREEN. |
| S013; matrix:L35; P:L472 | fixed-policy `CLOSE.md` — **KEEP CORE** | M04.P1-P4. Close zachowuje refresh, publication/readback i terminal custody, nie tylko merge command. |
| S014; matrix:L36; P:L473 | fixed-policy `RECOVERY.md` — **GENERALIZE** | M03.P4 + M04.P3. Recovery nie zależy od runtime binding lub starego worker; istniejący result jest reconciled. |
| S015; matrix:L37; P:L474 | fixed-policy `ROUTER.md` + root `CONTEXT_ROUTING.md` — **GENERALIZE** | M01.P2/P4. Small router ma exact entry/binding i precedence; nie potrzebuje preload całego drzewa. |
| S016; matrix:L38; P:L475 | `workflow/common/USER_STOP.md` — **GENERALIZE** | M02.P3 + M05.P1. Stop formatting i locator-only handoff zachowane bez Context Health variant. |
| S017; matrix:L39; P:L476 | `workflow/common/AUTHORITY.md` — **KEEP CORE** | M01.P2. Authority domains, durable truth i proportionality są core, nie optional bootstrap advice. |
| S018; matrix:L45; P:L477 | `workflow/contracts/PROJECT_REPOSITORY.md` / fixed-policy `REPOSITORY.md` — **GENERALIZE** | M01.P1/P2. PROJECT/navigation/state separation zachowane bez execution-policy field i root live board. |
| S019; matrix:L46; P:L478 | one project = one repository — **KEEP CORE** | M01.P1. Jedno consumer repo; source/V2 construction exception jest ograniczone i kończone transferem. |
| S020; matrix:L47; P:L479 | branch-first manifest-bound workstreams — **KEEP CORE** | M01.P2. Branch i manifest identyfikują exact workstream przed durable change; fixtures sprawdzają mismatch. |
| S021; matrix:L48; P:L480 | mutable repository-global workstream registry — **DROP** | M01.P4. DROP authoritative global registry; zwykły indeks nawigacyjny nie uzyskuje correctness ownership. |
| S022; matrix:L49; P:L481 | stacked parent/child workstreams — **KEEP CORE** | M04.P3. Oba legalne stacked paths zachowane; usunięcie parent nie może usunąć jedynej drogi recovery. |
| S023; matrix:L50; P:L482 | `WORKSTREAM.yaml` final-integration/cleanup ownership — **GENERALIZE** | M04.P1/P3. Final review/cleanup ma manifest owner; nie przeniesiono mutable ownership do Task Card. |
| S024; matrix:L51; P:L483 | `TASK_BOARD.yaml` mutable state — **KEEP CORE** | M03.P2. Board pozostaje mutable execution owner w wybranym workstream, nie globalnym pliku. |
| S025; matrix:L52; P:L484 | stable Task Card vs mutable Task Board — **KEEP CORE** | M03.P1/P2. Scope/tests stabilne, status/results mutable; zakaz konkurujących mirrors ma test. |
| S026; matrix:L53; P:L485 | root/default legacy Task Board as live destination — **DROP** | M06.P1/P2. Root legacy board tylko input migracji; normal fallback jest odrzucony. |
| S027; matrix:L54; P:L486 | execution-policy field — **DROP** | M01.P4 + M06.P2. DROP nowego selector; historyczna wartość nie jest legalnym V2 routing key. |
| S028; matrix:L55; P:L487 | runtime/model/session/worker identity in canonical state — **DROP** | M01.P4 + M03.P4. DROP canonical telemetry nie usuwa wymaganej semantic independence evidence. |
| S029; matrix:L56; P:L488 | durable orchestration binding — **DROP** | M01.P4 + M06.P2. DROP orchestration binding; konwersja ma zachować semantyczne pozostałości pracy. |
| S030; matrix:L57; P:L489 | universal `active_execution` / `transfer_ready` — **DROP** | M01.P4 + M06.P2. DROP wrapperów obejmuje dodatkowo ordinary returned; result można zachować do reconciliation. |
| S031; matrix:L58; P:L490 | Project-Card parallel batch/lane scheduler — **DROP** | M01.P4 + M03.P2. DROP Card scheduler obejmuje lanes/frozen-members/write-scope scheduler fields; nie zwykły scope bezpieczeństwa. |
| S032; matrix:L59; P:L491 | runtime-internal parallel subagents — **KEEP OUTSIDE PW** | M03.P2. Concurrency pozostaje poza PW schedulerem; workers nie tworzą dodatkowych Cards ani writers. |
| S033; matrix:L60; P:L492 | cumulative milestone handoff/checkpoint — **KEEP CORE** | M03.P4 + M04.P3. Milestone checkpoint jest wymagany także przy immediate continuation (§5); proporcjonalność nie znosi tego obowiązku. |
| S034; matrix:L61; P:L493 | terminal target-side workstream package — **KEEP CORE** | M04.P3. Unikalny terminal package poprzedza merge; późne bookkeeping odzyskiwane z target/merge evidence. |
| S035; matrix:L62; P:L494 | branch cleanup `safe_to_delete` fallback — **KEEP CORE** | M04.P3. Fallback jest wyzwalany tylko dla surviving safe ref; exact-head i absence readback pozostają. |
| S036; matrix:L68; P:L495 | `workflow/contracts/TASK_CARDS.md` + fixed-policy `TASK_CARDS.md` — **GENERALIZE** | M03.P1. Card ma authority, scope, tests oraz readback/review obligations; nie sam opis zadania. |
| S037; matrix:L69; P:L496 | `workflow/contracts/TASK_EXECUTION.md` — **GENERALIZE** | M03.P1/P2/P4. Refresh/start/DoD/blocker/review przetrwały usunięcie scheduler machinery. |
| S038; matrix:L70; P:L497 | `workflow/contracts/GITHUB_STATE.md` — **GENERALIZE / SHRINK** | M01.P2 + M04.P2/P3. Git state shrink nie usuwa recovery/ref/evidence safety; scheduler nie jest warunkiem trwałości. |
| S039; matrix:L71; P:L498 | `workflow/common/OPENSPEC.md` + `workflow/contracts/OPENSPEC.md` — **TRIGGER-ONLY / GENERALIZE** | M03.P1. Optional technical contract wymaga brakującej wartości ponad Card; tool-neutral/JIT zachowane. |
| S040; matrix:L72; P:L499 | speculative distant OpenSpec — **DROP** | M03.P1. DROP speculative distant OpenSpec; predecessor evidence określa moment szczegółowego kontraktu. |
| S041; matrix:L73; P:L500 | OpenSpec as replacement for requirements/plan/Card — **DROP** | M03.P1. DROP replacement authority; technical contract nie może nadpisać Definition, planu lub Card. |
| S042; matrix:L79; P:L501 | REQUIRED / RECOMMENDED exact-subject implementation review — **KEEP CORE** | M03.P3. Oba aktywowane review classes blokują do independent GREEN; RECOMMENDED nie oznacza późniejszego pominięcia. |
| S043; matrix:L80; P:L502 | product-specific reviewer identities — **DROP** | M03.P3/P4. DROP product identity jako kryterium independence; semantic production/repair nadal dyskwalifikuje. |
| S044; matrix:L81; P:L503 | Stage-6 planner spawning internal reviewer — **DROP** | M02.P3. DROP planner-spawned Stage-6; generic Stage-9 capability nie tworzy wyjątku od B. |
| S045; matrix:L82; P:L504 | Stage-9 internal independent reviewer when capability exists — **KEEP CORE** | M03.P3. Capability-first Stage-9 zachowany i sprawdzany realnym L08, nie sztucznym stopem. |
| S046; matrix:L83; P:L505 | locator-only fresh ChatGPT handoff — **KEEP CORE** | M05.P1. Locator-only dotyczy rzeczywistego fresh gate; nie wymusza dodatkowego kontekstu bez potrzeby. |
| S047; matrix:L84; P:L506 | Context Health / FRESH lifecycle — **DROP** | M01.P4. DROP Context Health/FRESH; ordinary context loss odtwarza durable obligations. |
| S048; matrix:L85; P:L507 | issue auto-implementation from initial `#issue` — **DROP** | M02.P1. DROP initial-issue auto-repair; safety question nie jest approval. |
| S049; matrix:L86; P:L508 | user stop at deployment/live-write merely because it is deployment/live-write — **DROP** | M04.P2/P4. DROP deployment-only stop; accepted authorization nadal jest honorowana. |
| S050; matrix:L92; P:L509 | GitHub as durable commit/PR/evidence source — **KEEP CORE** | M01.P1 + M04.P2. Immutable Git/PR/evidence i readback pozostają nośnikiem trwałości; nie dodano state database. |
| S051; matrix:L93; P:L510 | coherent commits / branch-PR managed changes — **KEEP CORE** | M01.P1 + M04.P1. Branch/PR po empty-root initialization; kontrolny commit nie jest proof V2 delivery. |
| S052; matrix:L94; P:L511 | never force-push main as normal remediation — **KEEP CORE** | M04.P1. Zakaz normal remediation force-push main i przepisywania published history zachowany także w rollback. |
| S053; matrix:L95; P:L512 | integration refresh against current target — **KEEP CORE** | M04.P1. Refresh występuje przed freeze/reuse i integration; nie tylko po merge. |
| S054; matrix:L96; P:L513 | textual merge cleanliness = semantic compatibility — **DROP** | M04.P1. DROP clean-merge equivalence; wymagane affected semantic/compatibility checks. |
| S055; matrix:L97; P:L514 | external `ACTION/WRITE -> READBACK -> VERIFY -> EVIDENCE` — **KEEP CORE** | M04.P2. Sekwencja effect/readback/verify/evidence obejmuje merge, publikację i tracker. |
| S056; matrix:L98; P:L515 | uncertain interrupted external side effect -> blind retry — **DROP** | M04.P2. DROP blind retry; ambiguous occurrence blokuje tę operację zamiast duplikować efekt. |
| S057; matrix:L99; P:L516 | GitHub auto-delete merged branch — **KEEP CORE** | M04.P3. Autodelete zaakceptowane jako normalne cleanup; źródło nie musi być odtworzone dla bookkeeping. |
| S058; matrix:L105; P:L517 | `workflow/common/FORK_RELEASE_VERSIONING.md` — **TRIGGER-ONLY** | M04.P4. Optional module ładuje się tylko przy declared downstream-fork release/version trigger. |
| S059; matrix:L106; P:L518 | `vX.Y.Z-private.N` lineage rules — **TRIGGER-ONLY** | M04.P4. Lineage zachowuje numeric lane/tuple, immutable history i native latest; nie narzuca tych wersji samemu V2. |
| S060; matrix:L107; P:L519 | competing research/prototype branches — **TRIGGER-ONLY** | M02.P2 JIT. Prototype branches są opcjonalnym Research narzędziem dla realnych alternatyw, nie kolejnym schedulerem. |
| S061; matrix:L108; P:L520 | `BLOCKER.md` durable blocker record/template — **KEEP SUPPORT** | M03.P4. Blocker record powstaje dla recovery value; nie każdy problem jest human stop. |
| S062; matrix:L109; P:L521 | acceptance evidence template — **KEEP SUPPORT** | M03.P4. Evidence template jest optional formą, nie opcjonalnością wymaganych dowodów. |
| S063; matrix:L115; P:L522 | `workflow/chatgpt/CAPABILITY_GATE.md` — **DROP as product gate** | M01.P4. DROP product gate; common capability decisions nie wybierają mixed policy. |
| S064; matrix:L116; P:L523 | `workflow/chatgpt/EXECUTION.md` — **GENERALIZE/MINIMIZE** | M05.P1 + M03.P2. Minimal ChatGPT UX/entry pozostało; nie powstała oddzielna semantic Execution. |
| S065; matrix:L117; P:L524 | `workflow/codex/CODEX_ORCHESTRATION.md` — **GENERALIZE/MINIMIZE** | M03.P2. Runtime-owned orchestration boundary zachowana; binding i Card parallelism usunięte. |
| S066; matrix:L118; P:L525 | `workflow/codex/EXECUTION.md` — **GENERALIZE/MINIMIZE** | M05.P2 + M03.P2. Codex różni delivery/realization, nie znaczenie Card, review lub recovery. |
| S067; matrix:L119; P:L526 | `workflow/codex/HANDOFF.md` — **MOSTLY DROP** | M05.P1 + M03.P4. Częściowy DROP jest precyzyjny: brak transfer lifecycle, ale useful locator/recovery principles zachowane. |
| S068; matrix:L120; P:L527 | named Codex Main/Executor/Tester/Investigator in canonical policy — **DROP** | M03.P2/P3. DROP concrete runtime role catalog; generic Main semantic responsibility nie jest zakazanym worker identity. |
| S069; matrix:L126; P:L528 | `.codex-plugin/plugin.json` — **BOOTSTRAP** | M05.P2. Manifest jest packaging-only; support syntax jest empirycznie sprawdzana przed pełną budową. |
| S070; matrix:L127; P:L529 | marketplace metadata — **BOOTSTRAP** | M05.P2/P3. Marketplace służy dystrybucji; source disambiguation i update nie tworzą policy authority. |
| S071; matrix:L128; P:L530 | `skills/project-workflow/SKILL.md` — **BOOTSTRAP** | M05.P2. Skill ma przyjętą nową nazwę i thin pointer; exact invocation pozostaje live gate. |
| S072; matrix:L129; P:L531 | `hooks/session-start.py` + `hooks.json` — **BOOTSTRAP** | M05.P2. Hook wskazuje local bundled router; brak routera/trust/path problem nie uruchamia remote policy reconstruction. |
| S073; matrix:L130; P:L532 | Codex fetching remote workflow repo in normal operation — **DROP** | M05.P2. DROP normal remote workflow fetch; read-only GitHub evidence projektu nie jest tym zakazanym policy acquisition. |
| S074; matrix:L131; P:L533 | `prompts/CHATGPT_PROJECT_INSTRUCTIONS.md` — **BOOTSTRAP** | M05.P1. Instrukcje ChatGPT są minimalne i user-owned; nie druga kopia workflow. |
| S075; matrix:L132; P:L534 | `prompts/CHATGPT_START.md` — **SHRINK / OPTIONAL** | M05.P1 JIT. SHRINK/OPTIONAL respektowane: wygodny prompt nie staje się mandatory authority module. |
| S076; matrix:L133; P:L535 | `prompts/CHATGPT_FRESH_SESSION.md` — **KEEP SUPPORT** | M05.P1. Fresh-session template ograniczone do locatorów rzeczywistego gate, bez powielania checklist. |
| S077; matrix:L134; P:L536 | `prompts/CODEX_START.md` — **DROP / DEBUG-ONLY** | M05.P2. DROP normal CODEX_START semantics; debug convenience, jeżeli potrzebne, nie wybiera current-main policy. |
| S078; matrix:L135; P:L537 | duplicate semantic policy inside plugin Skill/hook — **DROP** | M05.P2/P3. DROP duplicated policy; L05 celowo nie zmienia Skill/hook przy zmianie canonical module. |
| S079; matrix:L136; P:L538 | project-local plugin/MCP/Skill provisioning — **OUT OF SCOPE** | M05.P2. OUT OF SCOPE nie oznacza niewiadomego ownera: provisioning pozostaje przy newproject-skill. |
| S080; matrix:L142; P:L539 | `templates/PROJECT.md` — **GENERALIZE** | M01.P2. PROJECT template zawiera common marker/navigation, nie live phase/Card registry. |
| S081; matrix:L143; P:L540 | `templates/BRAINSTORM.md` — **KEEP SUPPORT** | M02.P2. Brainstorm template zachowuje decyzje/promoted revision, nie pełny transcript. |
| S082; matrix:L144; P:L541 | `templates/OPEN_QUESTIONS.md` — **KEEP SUPPORT** | M02.P2 JIT. Open questions są optional i material; nie nowy globalny decision database. |
| S083; matrix:L145; P:L542 | `templates/RESEARCH.md` — **KEEP SUPPORT** | M02.P2. Research template wymusza source weight/origin/return, nie tylko listę URL. |
| S084; matrix:L146; P:L543 | `templates/REQUIREMENTS.md` — **KEEP SUPPORT** | M02.P2. Requirements template zachowuje accepted revision/acceptance authority. |
| S085; matrix:L147; P:L544 | `templates/DECISION.md` — **KEEP SUPPORT** | M02.P2. Decision template zachowuje zaakceptowane rationale i consequences. |
| S086; matrix:L148; P:L545 | `templates/MASTER_PLAN.md` — **KEEP SUPPORT** | M02.P3. Plan template utrzymuje revision/coverage/milestones/gates/JIT; lifecycle review jest osobno. |
| S087; matrix:L149; P:L546 | `templates/MILESTONE.md` — **KEEP SUPPORT / OPTIONAL** | M03.P1 JIT. Milestone extension tylko gdy wnosi wartość; nie automatyczny duplikat planu. |
| S088; matrix:L150; P:L547 | `templates/TASK_CARD.md` — **KEEP SUPPORT** | M03.P1. Task Card template zachowuje bounded authority/scope/tests; proste zmiany mogą na nim poprzestać. |
| S089; matrix:L151; P:L548 | `templates/TASK_BOARD.yaml` — **GENERALIZE** | M01.P2 + M03.P2. Board template ma dokładny manifest binding; wyklucza canonical runtime/scheduler. |
| S090; matrix:L152; P:L549 | `templates/ACCEPTANCE_EVIDENCE.md` — **KEEP SUPPORT** | M03.P4. Optional evidence format nie osłabia exact actual/expected/result evidence. |
| S091; matrix:L153; P:L550 | `templates/BLOCKER.md` — **KEEP SUPPORT** | M03.P4. Optional blocker artifact ma exact owning obligation i recovery value. |
| S092; matrix:L154; P:L551 | `templates/HANDOFF.md` — **GENERALIZE** | M03.P4 + M05.P1. Rozróżniono cumulative checkpoint od świeżego locator-only promptu; nie zastępują się wzajemnie. |
| S093; matrix:L185; P:L552 | Official GitHub Issue for `#issue` — **KEEP SUPPORT / DEFAULT TRACKER** | M02.P4. Issue tracker dedup/correlation zachowane bez przyznania prawa do implementacji. |
| S094; matrix:L186; P:L553 | Official GitHub Issue for `#feature` — **KEEP SUPPORT / DEFAULT TRACKER** | M02.P4. Feature tracker może być doprecyzowany podczas discovery; nie jest zatwierdzeniem scope. |
| S095; matrix:L187; P:L554 | Workstream -> GitHub Issue exact reference — **KEEP CORE POINTER** | M02.P4. Exact Issue/repo/workstream/PR reference zachowane w state; nie zależy od rozmowy. |
| S096; matrix:L188; P:L555 | Final PR closing keyword — **KEEP SUPPORT** | M04.P2. Closing keyword ograniczony do final whole-scope default-branch PR; intermediate linkage jest testem negatywnym. |
| S097; matrix:L189; P:L556 | Post-merge Issue readback — **KEEP CORE CLOSE CHECK** | M04.P2. Post-merge readback jest obowiązkiem Close; fallback explicit close wymaga durable accepted completion. |

#### 7.1 Osobny audyt explicit DROP assertions

Frozen checklist ma 20 pozycji (matrix:L160–179). Wszystkie są normatywnie przeniesione przez P:L558 do A17, a poniższe obszary dają im sprawdzalną treść. To kontrola normal production semantics; cytaty, historia i migration input mogą zawierać zakazane nazwy bez aktywowania ich znaczenia.

| DROP | Konkretna negatywna granica / plan |
|---|---|
| D01 — fixed `chatgpt_only` tree | §3/M01/M05: common workflow; historyczny V1 controller nie jest V2 production tree. |
| D02 — fixed `codex_only` tree | §3/M01/M05: Codex posiada delivery, nie osobny semantic lifecycle. |
| D03 — legacy shared route | M06/A02: reader tylko dla requested migration; zwykły router nie wybiera legacy. |
| D04 — `execution_policy` | M01.P4/M06.P2: nielegalny selector w nowych templates/state. |
| D05 — mixed Capability Gate | S063/M01.P4: capability ustala realization wspólnego obowiązku, nie policy. |
| D06 — Context Health/FRESH | §3.2/M01.P4: restart odzyskuje durable obligation, nie odpala nowego lifecycle. |
| D07 — Project-Card parallelism | M03.P2/A04: dwie executing Cards w selected workstream odrzucone. |
| D08 — batch/lane/frozen-member metadata | M01.P4/M03.P2: brak scheduler schema mimo runtime-internal concurrency. |
| D09 — `parallel_safe` i scheduler write-scope fields | S031/P:L558: wykluczony concurrency contract Cards; bounded authority/scope sam w sobie jest zachowany. |
| D10 — universal `active_execution` | §3.1/M01.P4/M06: normal V2 state nie wymaga wrappera, historyczny input nie przechodzi do outputu. |
| D11 — `transfer_ready` | Jak D10; runtime change nie jest osobną fazą projektu. |
| D12 — durable orchestration binding | M03/M06: żadnego wyboru runtime harness w canonical truth. |
| D13 — canonical runtime/model/session/worker identity | M01/M03: semantic evidence zamiast identity; package test observations nie są routing state. |
| D14 — named product-specific implementation/reviewer roles | M03: generic responsibility dozwolone, konkretny role/model catalog poza PW. |
| D15 — automatic `#issue -> repair` | M02.P1/L02: późniejsza aligned authorization; safety question nie odblokowuje mutacji. |
| D16 — planner-spawned Stage-6 review | M02.P3/L07: frozen plan → B → fresh independent context. |
| D17 — unconditional deployment/live-write stop | M04.P4/§8: stop wynika z przyjętej authority, nie nazwy operacji. |
| D18 — duplicate plugin semantic policy | §3/M05.P3/L05: canonical module update bez Skill/hook policy edits. |
| D19 — ordinary Codex remote policy fetch | M05.P2/L04: local installed workflow; missing router fail-closed. |
| D20 — source branch required for terminal recovery | M04.P3/A10: target-side package i immutable merge evidence, również po autodelete. |

Dodatkowy zakaz **ordinary `returned`** z REQ-023 jest literalnie obecny w P:L128, L263, L489 i L558. Nie został pominięty dlatego, że 20-punktowy standalone checklist go nie powtarza. Pozostałe DROP w 97 wierszach — global registry, root live board, speculative/replacement OpenSpec, clean-merge-only compatibility, blind retry i normal CODEX_START — mają osobne negatywne assertions w odpowiednich S-wierszach.

### 8. Audyt pełnej validation matrix

**A01–A17: wszystkie strategicznie pokryte; żaden test nie został wykonany w tym review.** §6.1 ma pełne ID, a milestone acceptance i §6 doprecyzowują oracles, fixtures oraz związek z rzeczywistą implementacją.

| ID | Dokładny plan / owner | Ocena oracle i ryzyko, które musi wykryć |
|---|---|---|
| A01 | P:L298; M01.P4/M05.P2/P3 | Read sets od bootstrap po exact refs; unrelated modules nie mogą być obligatoryjne. Live trace uzupełnia automat. |
| A02 | L299; M01.P4/M06.P2/M07.P1 | Parsed state i reachability, nie samo wystąpienie forbidden słowa. Migration input nie jest positive route. |
| A03 | L300; M01.P2/P4/M04.P3 | Branch/ID/class/path/missing record odrzucone; legal terminal entry nie może być mylone z błędnym binding. |
| A04 | L301; M03.P2/P4 | Dwie Cards odrzucone, wielu runtime workers wewnątrz jednej dozwolone; sole state writer. J07. |
| A05 | L302; M03.P4/M06.P3 | Utrata worker po trwałym result prowadzi do verify/reconcile, nie ponownego wykonania. |
| A06 | L303; M04.P2/M06.P3 | Timeout po skutecznym write i nierozstrzygnięty readback to odrębne cases; retry nie może dublować efektu. |
| A07 | L304; M03.P3/P4 | S1/RED pozostaje immutable; S2 to nowy attempt, z valid independence i exact result check przed finalizacją. |
| A08 | L305; M04.P1 | SHA-only change zachowuje review tylko przy niezmienionym covered content/acceptance i GREEN compatibility. |
| A09 | L306; M04.P1 | Material reconciliation unieważnia stare coverage i wymaga nowego subjectu; nie ma clean-merge shortcut. |
| A10 | L307; M04.P3 | Source usunięte przed bookkeeping; target recovery nie odtwarza branch. J05 obejmuje reachability. |
| A11 | L308; M03.P1 | Obie strony selektywności: precyzyjny simple Card wystarcza, materialny extra contract jest wyzwalany JIT. |
| A12 | L309; M02.P2/M03.P1 | Reject speculative registry/extension, lecz retain potrzebne current security/correctness/testing. |
| A13 | L310; M02.P2 | Source breadth, weighting, conflicts/limits i brak official-only shortcut. Brak danej klasy źródeł wymaga uczciwego rozpoznania dostępności. |
| A14 | L311; M02.P4/M04.P2 | Exact existing Issue/workstream recovered; ambiguity/creation timeout nie usprawiedliwia duplikatu; intermediate open. |
| A15 | L312; M06.P1–P3 | Finite conversions, nieznany input fail-closed, preserved obligations i repeat/crash behavior. J06. |
| A16 | L313; M04.P4 | Concrete trigger; numeric lane/tuple, immutable history i native alias. Nie zwykły highest-SemVer resolver. |
| A17 | L314; M07.P1 i właściciele milestones | Wszystkie 97 oraz standalone drops wymagają implemented assertion albo jawnego non-code disposition; sama tabela nie wystarcza. |

Uzupełnienia P:L316 są potrzebne i mieszczą się w Definition: issue alignment/promotion, A/B/C/replan, role vs end-of-scope, authorization, stacks, changed cleanup head, read-only diagnosis, Research return crash, missing authority/trust i custody interruption. Nie tworzą dodatkowego wymagania ręcznego drivingu.

**L01–L09: wszystkie zachowane jako rzeczywiste mandatory acceptance, a nie obecne PASS.** M05/M07 mają właściwe prerequisites; wcześniejsze foundations A01–A04 albo package/context A17 nie są przedstawione jako ukończenie całej validation matrix.

| ID | Dokładny plan / etap | Ocena zachowania frozen live oracle |
|---|---|---|
| L01 | P:L322; M05 po M02 | Normal ChatGPT Android Project, repo authority, feature tracker, intrinsic numbered/recommended grilling, Research when needed, brak implementation. Zwykły syntetyczny chat nie zastępuje surface proof. |
| L02 | L323; M05 po M02/M03 | Symptom-only issue → diagnosis → safety question → dalsza rozmowa → dopiero aligned authorization. Ściślej chroni wymagany human boundary niż test dowolnej drugiej wiadomości. |
| L03 | L324; M05 po M04 | Intermediate PR/commit nie zamyka Issue; final default-branch linkage, actual Issue readback, accepted-completion-only explicit fallback, recovery bez duplikatu. Łączenie z L02 zachowuje oba oracles. |
| L04 | L325; M05 po M01 probe | Exact invocation, local bundle, thin loading i broken/missing router fail-closed. Opcjonalny smoke w matrix C nie znosi tego obowiązku (§6.2 L332). |
| L05 | L326; M05 z L04 | Canonical-only change, stałe bootstrap hashes, supported update i fresh-session installed readback. Cache/source ambiguity jawnie sprawdzana. |
| L06 | L327; M07 | ChatGPT → Codex → ChatGPT na tej samej authority/Card/review i bez state conversion; completed result reused. Sama identyczność serializacji nie wystarcza. |
| L07 | L328; M07 | Rzeczywiste A/B/C i fresh independent planning review; recovery re-presents gates. GREEN reviewer nie przechodzi do Prep przed C. |
| L08 | L329 i M07.P3 L281/286 | Jedna capable coordinating invocation: independent RED → bounded correction → independent GREEN → deterministic finalization. Delegation wymagana, gdy qualifying capability istnieje; brak artificial verdict-only stop. |
| L09 | L330 i M07.P3 L281 | Pierwszy fresh chat RED → same-chat authorized correction → nowy frozen subject i dopiero independence stop; drugi GREEN → same-chat finalization. Nie może zatrzymać się tylko z powodu RED/GREEN. |

Dodatkowy odczyt N authority potwierdził `topology-n: BAD\n` → `topology-n: GOOD\n`, immutable S1/S2, zachowanie RED, independence per subject i finalization bez replay. Plan przenosi te oracles do realnego V2, nie aktywuje starego harness ani `active_execution`. L08/L09 dotyczą Stage-9 i nie osłabiają premium Stage-6. Brak dostępnego capable runtime pozostawia L08 blocked i blokuje first production acceptance.

### 9. Pozostałe ryzyka i granica werdyktu

Największe ryzyko po GREEN to realizacja wymaganych dowodów: faktyczne zachowanie pluginu i agentów, poprawna equivalence review coverage, trwałość terminal refs i crash-safe custody/migration. Plan nie dowodzi jeszcze ich działania; nakazuje je zweryfikować przed odpowiednim odbiorem. J01–J08 nie dopisują nowej strategii ani nowych product choices. Ograniczają możliwe błędne interpretacje podczas kontraktowania już zaplanowanej pracy.

Ocena nie daje podstaw do skrócenia mandatory tests, pominięcia review, uznania źródła za niezależne po jego naprawie, zmiany przyjętej invocation albo rozszerzenia adoption poza scoped pilot. Szerszy rollout nie jest domyślną kontynuacją. Jednocześnie nie ma podstaw do wymagania dodatkowego repo-control system, universal event ledger, pełnej API schema w Master Planie lub obowiązkowego OpenSpec dla każdego Card.

**Werdykt końcowy pozostaje GREEN.** Żadna z podjętych prób zakwestionowania planu nie wykazała materialnej luki wymagającej strategic-plan revision. Wymagane następne czynności tego eksperymentu ograniczają się do finalnego odczytu niniejszego zapisu i ponownego potwierdzenia subject blob `0d55b03e2a4d1a2b1a4fd9972f8365f693262503`, po czym obowiązuje STOP. Ten record nie konsumuje canonical review approval, nie wykonuje meta-syntezy i nie rozpoczyna Execution Prep.
