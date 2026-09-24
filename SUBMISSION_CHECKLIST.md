# Checklist de Submissão – Aeternvm Vacuvm

## 1. Preparação para GitHub

- [x] Estrutura de pastas limpa
- [x] README.md com disclaimer científico honesto
- [x] LICENSE (CC-BY-4.0)
- [x] Código com paths relativos e avisos de toy model
- [x] Dados em CSV puro
- [x] Figuras com nomes descritivos
- [x] Papers LaTeX com citations corrigidas e tom profissional

## 2. Preparação para Zenodo

1. Criar conta em https://zenodo.org
2. New Upload → Upload the entire `Aeternvm_Vacuvm/` directory as ZIP
3. Preencher:
   - Title: Aeternvm Vacuvm: Vacuum Depletion as the Origin of the CKM Unitarity Deficit (Trilogy)
   - Authors: Gustavo Alves Conde
   - Description: (copiar o Abstract do Paper I + disclaimer)
   - Keywords: CKM unitarity, Cabibbo angle anomaly, lattice QCD, vacuum depletion, beyond Standard Model
   - License: CC-BY-4.0
   - Related identifiers: link do GitHub
4. Publicar → obter DOI

## 3. Preparação para arXiv

- Categoria: hep-ph (primary), hep-lat (cross-list se desejar)
- Formato: source LaTeX + figures + ancillary (CSV + code)
- Título e abstract devem deixar claro o caráter exploratório/toy
- Após aprovação do Zenodo, citar o DOI no paper

## 4. Revistas Científicas (após arXiv)

Ordem sugerida de submissão:
1. Physical Review D
2. Journal of High Energy Physics (JHEP)
3. European Physical Journal C
4. Physics Letters B (versão curta)

**Não submeter a journals de cosmologia** (JCAP, etc.) – o tema não é cosmológico.

## 5. Avisos finais de integridade científica

- Nunca afirmar que as simulações são “Lattice QCD real”.
- Sempre mencionar “toy model” ou “illustrative Metropolis simulation”.
- Os valores de $V_{ud}(A)$ do Paper II devem ser apresentados como reanálise ilustrativa, não como resultado experimental novo.
- O parâmetro $\kappa_{\rm vac}$ é um fit, não uma medição.
