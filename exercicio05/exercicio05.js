// RESOLUÇÃO DO EXERCÍCIO 05
// Linguagem JavaScript

// Valores iniciais
let string_invertida = "";

// Função para inverter a string
function inverteString(string) {
  for (let i = 0; i < string.length; i++) {
    string_invertida += string[string.length - i - 1];
  }
  return string_invertida;
}

// Impressão das strings original e invertida
console.log(`A string original é: ${"Esta vaga será minha!"}`);
console.log(`A string invertida é: ${inverteString("Esta vaga será minha!")}`);
