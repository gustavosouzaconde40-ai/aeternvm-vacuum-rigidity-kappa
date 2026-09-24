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
- Os dados de \( V_{ud}(A) \) utilizados no Paper II são uma reanálise ilustrativa.
- O acoplamento \( \kappa_{\rm vac} \sim 5 \times 10^{-4} \) é um parâmetro efetivo ajustado para reproduzir o déficit observado; não constitui medição experimental de “rigidez do vácuo”.

O material é disponibilizado para discussão científica e reprodução dos resultados. Não deve ser apresentado como resultado estabelecido da Lattice QCD convencional.

---

## Principais Resultados

| Paper | Conteúdo | Resultado principal |
|-------|----------|---------------------|
| **I** | Extrapolação ao contínuo + scan de parâmetros | \( \kappa_{\rm vac} \simeq 5 \times 10^{-4} \) reproduz \( \Delta_{\rm CKM} \approx 0.0015 \) |
| **II** | Dependência com número de massa \( A \) | Slope \( -1.7 \times 10^{-5} \) por nucleon |
| **III** | Código toy de rede \( 16^4 \) | \( \langle \phi \rangle \approx 1.0 \), \( V_{ud}^{\rm eff} \approx 0.97371 \) |

---

## Estrutura do Repositório

```text
├── Paper_I_Aeternvm_Vacuvm.tex
├── Paper_II_Aeternvm_Vacuvm.tex
├── Paper_III_Aeternvm_Vacuvm.tex
├── Aeternvm_Vacuvm_Overview.tex
├── lattice_aeternvm_sim.py          # Simulador Python 16⁴
├── chroma_action_Aeternvm.xml       # XML ilustrativo
├── varredura_completa.csv
├── regiao_anomalia.csv
├── paperII_dados_A.csv
├── fig3_HMC_evolution.jpg
└── LICENSE

'''
python3 lattice_aeternvm_sim.py

'''
@software{conde2026aeternvm,
  author       = {Conde, Gustavo Alves},
  title        = {Aeternvm Vacuvm: Vacuum Depletion as the Origin of the CKM Unitarity Deficit},
  year         = {2026},
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.22929619},
  url          = {https://doi.org/10.5281/zenodo.22929619}
}
