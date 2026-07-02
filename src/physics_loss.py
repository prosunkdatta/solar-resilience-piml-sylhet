"""
Physics-Informed ML for Solar Microgrid Resilience — Sylhet
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Module: physics_loss.py
Author: Prosun Datta
Contact: prosunkdatta@gmail.com

Description:
    The three physics-informed penalty terms and the combined
    PIML loss function for QX-01.

    The complete loss function is:
        L_total = L_MSE + λ₁·L_max + λ₂·L_night + λ₃·L_monsoon

    where:
        L_max     — penalises predictions exceeding the
                    Shockley-Queisser thermodynamic upper bound
        L_night   — penalises non-zero predictions when the sun
                    is below the horizon (θ_z ≥ 90°)
        L_monsoon — penalises deviation from the rain-cooled and
                    moisture-attenuated expected output during
                    heavy rainfall hours (NOVEL TERM)

    All loss terms are differentiable PyTorch operations and
    remain within the computation graph for backpropagation.

References:
    [10] Luo et al. (2021) — PC-LSTM physics-constrained loss
    [11] Raissi et al. (2019) — PINN framework
    [46] Nazartalab & Alavi-Rad (2026) — hospital microgrid resilience

Usage:
    from src.physics_loss import piml_loss
    loss = piml_loss(P_pred, P_target, P_max, zenith_mask,
                     rain_mask, GHI_att, eta_cooled, A,
                     lambda_1, lambda_2, lambda_3)
"""

import torch
import torch.nn as nn


def l_max(P_pred: torch.Tensor,
          P_max: torch.Tensor) -> torch.Tensor:
    """
    Upper-bound physics penalty term.

    Penalises any prediction that exceeds the thermodynamically
    possible maximum PV output (Shockley-Queisser limit):

        L_max = mean( ReLU(P_pred - P_max)² )

    where P_max = GHI × η × A × (1 - γ × (T_cell - T_ref))

    Parameters
    ----------
    P_pred : torch.Tensor, shape (batch,)
        Model predictions [W or kW].
    P_max : torch.Tensor, shape (batch,)
        Thermodynamic maximum power [same units as P_pred].

    Returns
    -------
    torch.Tensor (scalar)
        L_max penalty value.
    """
    # TODO: implement
    pass


def l_night(P_pred: torch.Tensor,
            night_mask: torch.Tensor) -> torch.Tensor:
    """
    Nocturnal zero-output physics penalty term.

    Penalises any positive prediction when the solar zenith
    angle θ_z ≥ 90° (sun below horizon — physically impossible
    to generate PV power):

        L_night = mean( P_pred² × night_mask )

    Parameters
    ----------
    P_pred : torch.Tensor, shape (batch,)
        Model predictions.
    night_mask : torch.Tensor, shape (batch,), dtype=float
        Binary mask: 1.0 where θ_z ≥ 90° (night), 0.0 otherwise.

    Returns
    -------
    torch.Tensor (scalar)
        L_night penalty value.
    """
    # TODO: implement
    pass


def l_monsoon(P_pred: torch.Tensor,
              P_phys_monsoon: torch.Tensor,
              rain_mask: torch.Tensor) -> torch.Tensor:
    """
    Novel monsoon rain-cooling and attenuation penalty term.

    During heavy rainfall events, PV output is governed by a
    dual thermodynamic effect:
        (1) Rain-cooling: precipitation temporarily reduces cell
            temperature, boosting efficiency by ~0.5-1.5%
        (2) Moisture attenuation: airborne moisture and cloud
            cover reduce effective irradiance (GHI_att < GHI)

    This term penalises predictions that deviate from this
    physics-corrected expected output during rainfall hours:

        L_monsoon = mean( (P_pred - P_phys_monsoon)² × rain_mask )

    where:
        P_phys_monsoon = GHI_att × η_cooled × A
        GHI_att = GHI × attenuation_factor(RH2M, PRECIP)
        η_cooled = η × (1 + rain_cooling_boost)
        rain_mask = 1.0 where PRECIP > threshold, else 0.0

    This is the first published PIML loss term to capture this
    dual dynamic in a South Asian monsoon corridor.

    Parameters
    ----------
    P_pred : torch.Tensor, shape (batch,)
        Model predictions.
    P_phys_monsoon : torch.Tensor, shape (batch,)
        Physics-corrected expected output during rainfall.
    rain_mask : torch.Tensor, shape (batch,), dtype=float
        Binary mask: 1.0 where PRECIP > threshold, 0.0 otherwise.

    Returns
    -------
    torch.Tensor (scalar)
        L_monsoon penalty value.
    """
    # TODO: implement
    pass


def piml_loss(P_pred: torch.Tensor,
              P_target: torch.Tensor,
              P_max: torch.Tensor,
              night_mask: torch.Tensor,
              rain_mask: torch.Tensor,
              P_phys_monsoon: torch.Tensor,
              lambda_1: float = 0.1,
              lambda_2: float = 0.5,
              lambda_3: float = 0.3) -> torch.Tensor:
    """
    Combined Physics-Informed Machine Learning loss function.

        L_total = L_MSE + λ₁·L_max + λ₂·L_night + λ₃·L_monsoon

    Parameters
    ----------
    P_pred : torch.Tensor, shape (batch,)
        Model predictions.
    P_target : torch.Tensor, shape (batch,)
        Ground-truth PVLib-simulated PV power.
    P_max : torch.Tensor, shape (batch,)
        Thermodynamic maximum power per hour.
    night_mask : torch.Tensor, shape (batch,)
        1.0 at night hours (θ_z ≥ 90°), 0.0 otherwise.
    rain_mask : torch.Tensor, shape (batch,)
        1.0 during heavy rainfall, 0.0 otherwise.
    P_phys_monsoon : torch.Tensor, shape (batch,)
        Rain-corrected expected output during monsoon rainfall.
    lambda_1 : float
        Weight for L_max term. Default 0.1.
    lambda_2 : float
        Weight for L_night term. Default 0.5.
    lambda_3 : float
        Weight for L_monsoon term. Default 0.3.

    Returns
    -------
    torch.Tensor (scalar)
        Total PIML loss value.
    """
    # TODO: implement
    pass
