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

- As simulações de rede apresentadas são **modelos toy** (Metropolis simplificado em 16⁴). Não são simulações Lattice QCD completas com HMC, fermions dinâmicos e extrapolação controlada.
- Os dados de Vud(A) utilizados no Paper II são uma reanálise ilustrativa.
- O acoplamento kappa_vac ≈ 5×10⁻⁴ é um parâmetro efetivo ajustado para reproduzir o déficit observado. Não constitui medição experimental de “rigidez do vácuo”.

O material é disponibilizado para discussão científica e reprodução dos resultados. Não deve ser apresentado como resultado estabelecido da Lattice QCD convencional.

'''

## Principais Resultados

| Paper | Conteúdo                          | Resultado principal                     |
|-------|-----------------------------------|-----------------------------------------|
| I     | Extrapolação ao contínuo + scan   | kappa_vac ≈ 5×10⁻⁴ reproduz Δ_CKM ≈ 0.0015 |
| II    | Dependência com número de massa A | Slope ≈ −1.7×10⁻⁵ por nucleon           |
| III   | Código toy de rede 16⁴            | ⟨φ⟩ ≈ 1.0 , Vud_eff ≈ 0.97371           |

'''

## Estrutura do Repositório

```text
├── Paper_I_Aeternvm_Vacuvm.tex
├── Paper_II_Aeternvm_Vacuvm.tex
├── Paper_III_Aeternvm_Vacuvm.tex
├── Aeternvm_Vacuvm_Overview.tex
├── lattice_aeternvm_sim.py
├── chroma_action_Aeternvm.xml
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

'''

Licença
Documentos e dados: Creative Commons Attribution 4.0 International (CC-BY-4.0)
Código Python: MIT License

Contato
Gustavo Alves Conde
Baixo Guandu – ES – Brasil
Aeternvm Vacuvm Collaboration
