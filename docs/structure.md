# Structure Reference

## Priority Example

Use `assets/ВКР Антонов Илья 21ВП2 .docx` as the main structural and visual reference. Inspect it with `python-docx` when exact heading levels, section order, captions, or appendices are unclear.

The reference follows this high-level order:

1. `Содержание`
2. `Введение`
3. Раздел 1: analysis of subject area, algorithms/processes, analogous systems, task statement, requirements.
4. Раздел 2: system/software design.
5. Раздел 3: software development.
6. Раздел 4: software quality control, testing, metrics, planning and budget.
7. `Заключение`
8. `Список использованных источников`
9. Appendices: `Приложение А ...`, `Приложение Б ...`, etc.

Front matter such as personal notebook, assignment, and abstract may be excluded during drafting if the user asks to focus on core sections.

## Introduction

Purpose: justify relevance and lead to the goal and tasks.

Include:

- subject-area importance;
- current manual or insufficiently automated process;
- risks and consequences;
- need for the proposed system;
- goal of the ВКР;
- tasks of the ВКР.

Avoid:

- detailed technology stack;
- internal modules and class names;
- testing details;
- long implementation descriptions.

## Section 1: Analysis And Task Statement

Recommended title pattern:

`Анализ предметной области и постановка задачи на разработку ...`

Required subsections:

- subject-area analysis;
- analysis of the current process, method, or domain algorithm;
- analysis of analogous software or competing tools;
- task statement;
- requirements analysis.

Subject-area analysis should explain real actors, documents/data, workflows, information flows, and pain points. Use tables for actors, data/documents, process comparison, and competitor comparison.

Requirements analysis must include:

- use case diagram;
- functional requirements table;
- use case specifications as tables;
- nonfunctional requirements table;
- clear conclusion leading into design.

## Section 2: Design

Recommended title pattern:

`Проектирование ...`

Include:

- architecture and justification;
- structural/data design;
- conceptual model;
- logical model;
- system workflow or deployment structure;
- hardware/software requirements.

Use UML component, class/ER, sequence/activity, and deployment diagrams where appropriate. Do not replace UML diagrams with arbitrary decorative schemes.

## Section 3: Software Development

Recommended title pattern:

`Разработка программного обеспечения ...`

Adapt to the actual application. Typical subsections:

- application/source-code structure;
- database/storage implementation;
- core service or algorithm implementation;
- document/report/output generation;
- user interface implementation;
- file/archive/integration implementation;
- launch, packaging, and deployment.

Write from codebase facts: real modules, real classes/services, real templates, real screenshots. Do not paste long code listings in the main text; move them to appendices.

## Section 4: Quality Control

Recommended title:

`Контроль качества программного обеспечения`

Use the example’s logic: testing model and quality metrics first, then concrete testing, then planning/budget.

Typical subsections:

- justification of testing model and quality metrics;
- functional testing of critical user scenarios;
- module and integration testing of services/components;
- manual UI testing when applicable;
- development planning and budget estimation.

Tables to include:

- risks and verification methods;
- testing types used in the project;
- test cases for critical scenarios;
- mapping of automated tests to components;
- manual UI checklist;
- development effort estimate;
- conditional budget estimate.

Figures may include:

- screenshot of test run;
- screenshots of key tested UI scenarios;
- Gantt chart;
- project work breakdown structure.

## Conclusion

Use `Title` style, no number.

Include:

- confirmation of problem relevance;
- completed analysis;
- defined requirements;
- designed architecture/model/scenarios;
- implemented application or module;
- completed testing;
- practical result;
- future development directions.

Write in past tense. Do not add new requirements or new implementation details not covered in the body.

## Sources

Use `Title` style, no number: `Список использованных источников`.

Sources should support:

- subject-area theory and domain rules;
- competitor/product analysis;
- UML and design methods;
- libraries/frameworks/tools used;
- software testing;
- project planning and Gantt/budget methods.

Prefer official documentation for technologies and official product pages for competitors. Include URL and access date for electronic sources.

## Appendices

Each appendix starts on a new page and uses `Title` style:

`Приложение А (справочное) Глоссарий`

or

`Приложение Б (рекомендуемое) ...`

Recommended appendices:

- glossary;
- database table attribute specifications;
- data model listings;
- core service listings;
- document/report generation listings;
- UI fragments;
- automated tests;
- additional testing screenshots.

Use appendix references in the main text only after the appendix exists or will be added in the same iteration.
