# Aeternvm Vacuvm – Trilogia Lattice QCD & Anomalia CKM

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.22929619.svg)](https://doi.org/10.5281/zenodo.22929619)

**Autor:** Gustavo Alves Conde  
**Colaboração:** Aeternvm Vacuvm Collaboration  
**Local:** Itaguaçu, ES, Brasil  
**Data:** Setembro 2026  
**Zenodo:** https://doi.org/10.5281/zenodo.22929619  

---

## Aviso Importante (Disclaimer)

Este repositório contém uma **proposta teórica exploratória** que reinterpreta a anomalia de unitariedade da matriz CKM (Cabibbo Angle Anomaly) como consequência de um vácuo deplecionável.

- As simulações de rede apresentadas são **modelos toy** (Metropolis simplificado em 16⁴), **não** simulações Lattice QCD completas com HMC, fermions dinâmicos e extrapolação controlada.
- Os dados de $V_{ud}(A)$ utilizados no Paper II são uma reanálise ilustrativa; a literatura oficial (Hardy & Towner) não reporta uma dependência em $A$ estatisticamente estabelecida no nível aqui reivindicado.
- O acoplamento $\kappa_{\rm vac}\sim5\times10^{-4}$ é um parâmetro efetivo ajustado para reproduzir o déficit observado; não constitui medição experimental de “rigidez do vácuo”.

O material é disponibilizado para discussão científica, reprodução dos plots e eventual desenvolvimento futuro. Não deve ser apresentado como resultado estabelecido da Lattice QCD convencional.

---

## Estrutura do Repositório

```
Aeternvm_Vacuvm/
├── README.md                          # Este arquivo
├── LICENSE                            # CC-BY-4.0
├── papers/
│   ├── Paper_I_Aeternvm_Vacuvm.tex    # Déficit CKM + extrapolação ao contínuo
│   ├── Paper_II_Aeternvm_Vacuvm.tex   # Dependência com número de massa A
│   └── Paper_III_Aeternvm_Vacuvm.tex  # Código toy de rede
├── code/
│   ├── lattice_aeternvm_sim.py        # Simulador Python 16⁴ (executável)
│   └── chroma_action_Aeternvm.xml     # XML ilustrativo (não é input Chroma completo)
├── data/
│   ├── varredura_completa.csv         # Scan de parâmetros
│   ├── regiao_anomalia.csv            # Pontos que fecham a anomalia
│   └── paperII_dados_A.csv            # Dados usados no fit A-dependence
├── figures/
│   ├── fig1_deficit_kappa.png
│   ├── fig2_A_dependence.jpg
│   ├── fig3_HMC_evolution.jpg
│   └── fig4_continuum_extrapolation.png
└── docs/
    └── (apresentações e notas adicionais)
```

---

## Como Compilar os Papers

Requer TeX Live com `revtex4-2`:

```bash
cd papers
pdflatex Paper_I_Aeternvm_Vacuvm.tex
pdflatex Paper_II_Aeternvm_Vacuvm.tex
pdflatex Paper_III_Aeternvm_Vacuvm.tex
```

As figuras devem estar no diretório `../figures/`.

---

## Como Rodar a Simulação Toy

```bash
cd code
python3 lattice_aeternvm_sim.py
```

Gera `paperIII_evolution.png` e `phi_final.npy`.

---

## Como Citar

Se utilizar este material, cite como:

> G. A. Conde, “Aeternvm Vacuvm: Vacuum Depletion as the Origin of the CKM Unitarity Deficit (Trilogy + Toy Lattice Code)” (2026).  
> **Zenodo:** https://doi.org/10.5281/zenodo.22929619  
> **GitHub:** [link do repositório após publicação]

---

## Submissão a Revistas / arXiv

**Categoria arXiv recomendada:**  
- `hep-ph` (fenomenologia)  
- `hep-lat` (apenas se a seção de métodos deixar explícito que se trata de modelo toy)

**Revistas adequadas (após peer-review rigoroso):**  
- Physical Review D (Particles, Fields, Gravitation, and Cosmology) – seção de fenomenologia  
- Journal of High Energy Physics (JHEP)  
- European Physical Journal C  

**Não recomendado como paper de cosmologia:** o tema é física de partículas / sabor / lattice, não cosmologia observacional ou teoria de inflação/energia escura.

Antes de submeter:
1. Substituir placeholders de arXiv (ex.: arXiv:2306.XXXX) pelas referências finais publicadas.
2. Deixar explícito em todo o texto que as simulações são ilustrativas.
3. Incluir os arquivos CSV e o código como material suplementar (ancillary files no arXiv ou Zenodo).

---

## Licença

Creative Commons Attribution 4.0 International (CC-BY-4.0).  
Código Python: MIT License.

---

## Contato

Gustavo Alves Conde  
Itaguaçu – ES – Brasil  
Aeternvm Vacuvm Collaboration
