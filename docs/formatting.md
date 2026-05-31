# Formatting Reference

## Base DOCX Rules

Use styles from the priority example DOCX. When creating a new document, start from the example or copy its styles.

Common settings:

- margins: left 3 cm, right 1 cm, top 2 cm, bottom 2 cm;
- body text style: `No Spacing`;
- font: Times New Roman 14 pt;
- alignment: justified;
- first-line indent: 1.25 cm;
- line spacing: 1.5;
- headings: `Title`, `Heading 1`, `Heading 2`, `Heading 3`;
- all heading styles must be bold.

## Table Formatting

Caption:

- style: `Таблица название`;
- format: `Таблица N – Наименование`;
- use an en dash/long dash, not a hyphen;
- caption is immediately above the table;
- caption paragraph must have `keep_with_next = true`.

Table body:

- Times New Roman 12 pt;
- single line spacing;
- no paragraph indentation inside cells;
- header row bold and centered;
- header row has Word repeat-header enabled (`w:tblHeader`);
- body cells usually align left unless numeric comparison needs another alignment.

Never insert a paragraph between a table caption and the table.

## Figure Formatting

Caption:

- style: `Рисунок или подрисуночная надпись`;
- format: `Рисунок N – Наименование`;
- caption is immediately under the figure;
- use an en dash/long dash, not a hyphen.

Figure paragraph:

- placed immediately before the caption;
- `keep_with_next = true`;
- `space_after = 10 pt`;
- no empty paragraph for visual spacing.

Never insert a paragraph between a figure and its caption.

## References In Text

Every table and every figure must have a prior narrative reference.

Good patterns:

- `... представлены в таблице N.`
- `... приведены в таблице N.`
- `... показана на рисунке N.`
- `... представлена на рисунке N.`
- `Спецификации ... представлены в таблицах N–M.`
- `Основные экраны ... показаны на рисунках N–M.`

Do not place a table or figure immediately after a heading without an introductory paragraph.

After a table or figure that supports analysis, design, or testing, add a short conclusion explaining what follows from it.

## TOC

The contents page:

- appears before `Введение`;
- has heading `Содержание`, style `Title`, centered and bold;
- uses an automatic Word TOC field, not manually typed lines;
- includes heading levels 1-3;
- is followed by a page break;
- `Введение` starts on a new page;
- document settings should enable `updateFields` so Word can prompt for field updates.

After adding sections, headings, figures, tables, or appendices, tell the user to update the TOC in Word.

## Page Breaks And Object Cohesion

Use paragraph properties, not empty paragraphs, for spacing.

Rules:

- table caption stays with the table;
- figure stays with the caption;
- no caption may be left alone at the bottom of a page;
- no figure caption may move to the next page without the figure;
- large tables may split across pages, but header rows must repeat.

If a visual check shows a separated caption/object pair, fix via `keep_with_next`, page break before caption/object, or by moving the preceding paragraph. Do not use multiple blank paragraphs.

## DOCX Verification Checklist

After editing a DOCX, verify:

- ZIP integrity: `unzip -t file.docx`;
- expected headings exist;
- table and figure numbering is continuous;
- captions use `–`, not `-`;
- each table/figure has a prior text reference;
- table captions have `keep_with_next`;
- figure paragraphs have `keep_with_next` and `space_after = 10 pt`;
- tables use 12 pt, single spacing, no cell paragraph indent;
- header rows are bold, centered, and repeat;
- heading styles are bold;
- no empty paragraphs were inserted for spacing;
- the TOC field still exists and `updateFields` is enabled.

Use targeted repairs if user-edited text exists. Do not regenerate a full document unless the user explicitly requests it.
