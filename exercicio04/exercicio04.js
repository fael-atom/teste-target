// RESOLUÇÃO DO EXERCÍCIO 04
// Linguagem JavaScript

// Faturamentos mensais por estado
const fat_sp = 67836.43,
  fat_rj = 36678.66,
  fat_mg = 29229.88,
  fat_es = 27165.48,
  fat_outros = 19849.53;

// Cálculo do faturamento total
const fat_total = (fat_sp + fat_rj + fat_mg + fat_es + fat_outros)

// Representatividade de SP (%)
let rep_sp = ((fat_sp / fat_total) * 100).toFixed(1);

// Representatividade do RJ (%)
let rep_rj = ((fat_rj / fat_total) * 100).toFixed(1);

// Representatividade de MG (%)
let rep_mg = ((fat_mg / fat_total) * 100).toFixed(1);

// Representatividade do ES (%)
let rep_es = ((fat_es / fat_total) * 100).toFixed(1);

// Representatividade dos demais estados (%)
let rep_outros = ((fat_outros / fat_total) * 100).toFixed(1);


// Tabela de Representatividade
console.log(`O percentual de representação de cada estado é:\n\n
SP - ${rep_sp}%\n
RJ - ${rep_rj}%\n
MG - ${rep_mg}%\n
ES - ${rep_es}%\n
Outros - ${rep_outros}%\n
`);