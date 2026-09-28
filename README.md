# Aeternvm Vacuvm – Trilogia Lattice QCD & Anomalia CKM

## V6.9 Update - Tractor-6 JWST Early Chemical Enrichment [NEW - 28-Sep-2026]

> **Discovery:** JWST/NIRSpec encontrou C, O, Si em 3 galáxias a z~7.3-9.3 (~500 Myr após Big Bang), com outflow em blueshift 50-250 km/s, baryon cycling ativo. Publicado em *Nature Astronomy*, resumido pelo canal Bariogênese.

**Correlação com Rigidez do Vácuo:**

Se vácuo fosse inerte, 500 Myr deveria ser pristino H/He. JWST mostra poluição rápida. No Aeternvm Vacuvm:

1. Trator-5 fixou kappa_vac = 5e-4 do déficit CKM Δ_CKM ≈ 0.0015 (Trabalho W = kappa<phi>)
2. Trator-6 mostra mesma depleção na aurora cósmica: SF intensa depleta vácuo local φ = 1 → 0.9995, barreira cai para síntese C/O/Si
3. Gradiente ∇φ empurra outflow - 50-250 km/s observados = pressão φ, não só vento estelar
4. Pop III escassa = esperado. Sorvete de baunilha nunca ficou branco. Z0 = 376.73 Ω denominador comum se mantém.

**Fórmula:** Lambda_eff(Z0, ∇I) = Z0 * f(|∇I|) | v_out ≈ c * kappa_vac * |∇φ| * 1e3 → 50-250 km/s

**Ref:** https://www.youtube.com/watch?v=snlvepcEv7M + Nature Astronomy

Veja `addendum_x5f_jwst_x5f_tractor6.md` para derivação completa.

---

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.22929619.svg)](https://doi.org/10.5281/zenodo.22929619)

**Autor:** Gustavo Alves Conde  
**Colaboração:** Aeternvm Vacuvm Collaboration  
**Local:** Baixo Guandu, ES, Brasil  
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
| **IV** | **GW170817 + Rigidez Z0 - Prova 7** | **κ=1,11±0,25, dotG/G<5,34e-10/yr => dotZ0/Z0<2,7e-10/yr, Barreira 10^53,5** |
'''

## Estrutura do Repositório

```text
├── Paper_I_Aeternvm_Vacuvm.tex
├── Paper_II_Aeternvm_Vacuvm.tex
├── Paper_III_Aeternvm_Vacuvm.tex
├── Paper_IV_Aeternvm_Vacuvm_GW170817.tex
├── Aeternvm_Vacuvm_Overview.tex
├── lattice_aeternvm_sim.py
├── trator5_kappa_GW170817.py
├── trator5_gw170817_proof.json
├── chroma_action_Aeternvm.xml
├── varredura_completa.csv
├── regiao_anomalia.csv
├── paperII_dados_A.csv
├── fig3_HMC_evolution.jpg
└── LICENSE
```


'''

## Como Rodar a Simulação Toy

```bash
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

'''

---

## V6.8 Update - Five-Tractor Proof Chain of Z0 = 376.73 Ω [NEW - 26-Sep-2026]

> Este repositório é o HEAD atual do formalismo. Esta seção nova conecta a Trilogia CKM acima com a batalha central do Z0.

**Manuscrito congelado China:** RAA-2026-0669 (26-Sep-2026) - Four-tractor depletion road: JWST to LHAASO 3.73 PeV - Research in Astronomy and Astrophysics - TAG v6.7.1-china-RAA-0669 - NÃO ALTERAR

**Versão atual:** V6.8 - Five-tractor with BESIII X(2370) glueball

### Cadeia de 5 Tratores - Denominador Comum Z0

1.  **Tractor-1 Conde Ruler:** I=log(1+rho/rho0), k=2*pi*Z0/S_inst=8.45 Ω (S_inst=280) - Modelo nulo imutável 1M gaps Z'=gap/ln(p) média 1.00041294 | DOI 10.5281/zenodo.22651450
2.  **Tractor-2 FAST-10P:** Z0=376.730313 Ω unidade natural | DOI 10.5281/zenodo.22821262
3.  **Tractor-3 JWST CEERS:** High-z excess = vácuo ativo larga escala
4.  **Tractor-4 LHAASO 3.73 PeV:** Cygnus X-3 tau_AV=0.81 <1 vs tau~4.5 = transparência anômala
5.  **Tractor-5 BESIII X(2370):** [NOVO] Glueball self-binding puro - M=2370 MeV J^PC=0^-+ flavor-singlet - Prova lab de Z-Bits saturados. Ref: https://www.youtube.com/watch?v=obqUOnfKi-Y (PIPA)

**Hierarquia de Repos:**
- Primary this repo: https://zenodo.org/records/22949508 -> V6.8 (rigidity kappa)
- Legacy: AETERNVMVACUVM / 22873164
- Null model: conde-governante / 22651450
- Evidence: VACUO-ATIVO-6-PROVAS / 22837427
- Lab: ENGINE / 22850558

**Proof:** JWST + IXPE PD=0.556 + LHAASO + LZ 2.6σ + BESIII X(2370) -> Lambda_eff(Z0, nabla I)=Z0 f(|nabla I|)

Data Availability: China-VO PaperData / ScienceDB per RAA.

### Pasta do 5º Trator
Ver `/tractor-5-BESIII-X2370-glueball-pure-self-binding/` com PDF isolado V6.8

