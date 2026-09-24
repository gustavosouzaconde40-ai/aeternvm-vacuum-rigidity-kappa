"""
Lattice Aeternvm Vacuvm - Mini Simulador 16^4 com campo phi de depleção
Paper III - Código demonstrativo executável
Author: Aeternvm Vacuvm Collaboration
"""

import numpy as np
import matplotlib.pyplot as plt

# Parâmetros da rede
L = 16
T = 16
beta = 6.0  # acoplamento QCD
kappa_vac = 0.0005  # melhor fit Paper I
lam = 0.1   # auto-acoplamento phi
v = 1.0     # vev phi

# Inicializa campos
np.random.seed(42)
U = np.random.randn(L,L,L,T,4) * 0.1  # links simplificados (fase)
phi = np.ones((L,L,L,T)) * v + np.random.randn(L,L,L,T)*0.05

def plaquette(U):
    # toy plaquette
    return np.mean(U**2)

def action_QCD(U):
    return beta * (1 - plaquette(U))

def action_phi(phi):
    # V = lambda(phi^2 - v^2)^2 + grad phi^2
    pot = lam * np.mean((phi**2 - v**2)**2)
    kinetic = 0.5*np.mean(np.gradient(phi)[0]**2)
    return pot + kinetic

def action_int(U, phi):
    # acoplamento Aeternvm: kappa phi Tr(F^2) ~ kappa phi U^2
    return kappa_vac * np.mean(phi) * np.mean(U**2)

def metropolis_step(U, phi, n_sweep=100):
    history = []
    for sweep in range(n_sweep):
        # update phi
        dphi = (np.random.rand(*phi.shape)-0.5)*0.1
        phi_new = phi + dphi
        dS = lam*np.mean((phi_new**2 - v**2)**2 - (phi**2 - v**2)**2) + kappa_vac*np.mean(dphi)*0.1
        if dS < 0 or np.random.rand() < np.exp(-dS*100):
            phi = phi_new
        # update U
        dU = (np.random.randn(*U.shape)-0.5)*0.05
        U_new = U + dU
        dS_qcd = beta*(np.mean(U_new**2)-np.mean(U**2))
        if dS_qcd < 0 or np.random.rand() < np.exp(-dS_qcd):
            U = U_new
        
        S_tot = action_QCD(U) + action_phi(phi) + action_int(U,phi)
        Vud_eff = 0.97420 * (1 - kappa_vac*np.mean(phi))
        history.append((S_tot, np.mean(phi), Vud_eff))
    return U, phi, np.array(history)

print(f"Rodando Lattice Aeternvm {L}^3 x {T} - beta={beta}, kappa={kappa_vac}")
U, phi, hist = metropolis_step(U, phi, n_sweep=200)

# Plots
fig, axs = plt.subplots(3,1, figsize=(8,9), sharex=True)
axs[0].plot(hist[:,0])
axs[0].set_ylabel('S_total')
axs[0].set_title(f'Lattice Aeternvm {L}^4 - Evolução HMC')

axs[1].plot(hist[:,1], color='orange')
axs[1].axhline(v, linestyle='--', color='gray')
axs[1].set_ylabel('<phi> (densidade vacuo)')

axs[2].plot(hist[:,2], color='red')
axs[2].axhline(0.97420, linestyle=':', label='Vud bare')
axs[2].axhline(0.97365, linestyle='--', color='gray', label='Vud com depleção')
axs[2].set_ylabel('Vud_eff')
axs[2].set_xlabel('Sweep HMC')
axs[2].legend()

plt.tight_layout()
plt.savefig('paperIII_evolution.png', dpi=300)
print("Figura salva: paperIII_evolution.png")

# Salva config final
np.save('phi_final.npy', phi)

print(f"<phi> final = {np.mean(phi):.5f}")
print(f"Vud_eff final = {hist[-1,2]:.5f}")
print(f"Deficit CKM final = {1 - (hist[-1,2]**2 + 0.2252**2):.5f}")

# Gera action.xml para Chroma (exemplo ilustrativo)
chroma_xml = f"""<!-- Illustrative XML for Aeternvm action - NOT a full Chroma input -->
<chroma>
<LatticeAeternvm>
  <lattice_size>{L} {L} {L} {T}</lattice_size>
  <beta>{beta}</beta>
  <kappa_vac>{kappa_vac}</kappa_vac>
  <lambda_phi>{lam}</lambda_phi>
  <vev>{v}</vev>
  <action> S = beta*Plaq + kappa*phi*Tr(F^2) + lambda*(phi^2-v^2)^2 </action>
  <phi_field>dynamical scalar - vacuum depletion field (toy model)</phi_field>
  <observable>Vud_eff = Vud_bare*(1-kappa*<phi>)</observable>
  <HMC>
    <n_sweeps>1000</n_sweeps>
    <trajectory_length>1.0</trajectory_length>
    <step_size>0.02</step_size>
  </HMC>
</LatticeAeternvm>
</chroma>
"""
with open('chroma_action_Aeternvm_illustrative.xml','w') as f:
    f.write(chroma_xml)

print("Arquivos gerados: paperIII_evolution.png, phi_final.npy, chroma_action_Aeternvm_illustrative.xml")
print("AVISO: Este e um modelo toy (Metropolis simplificado). Nao e uma simulacao Lattice QCD real.")
