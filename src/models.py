"""
Physics-Informed ML for Solar Microgrid Resilience — Sylhet
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Module: models.py
Author: Prosun Datta
Contact: prosunkdatta@gmail.com

Description:
    PyTorch model definitions for all architectures used in QX-01:
        - LSTMBaseline: standard LSTM with MSE loss only
        - GRUBaseline:  standard GRU with MSE loss only
        - PIMLModel:    LSTM with physics-informed custom loss
                        (L_MSE + λ₁L_max + λ₂L_night + λ₃L_monsoon)

    All models share the same architecture backbone:
        Input → 2-layer RNN (64 units, dropout 0.2) → Linear output

Usage:
    from src.models import LSTMBaseline, GRUBaseline, PIMLModel
    model = PIMLModel(input_size=11, hidden_size=64, num_layers=2)
"""

import torch
import torch.nn as nn


class LSTMBaseline(nn.Module):
    """
    Standard LSTM baseline for solar power forecasting.

    Architecture:
        - 2 LSTM layers, 64 hidden units per layer
        - Dropout 0.2 between layers
        - 1 linear output layer

    Loss: MSE only (no physics constraints)

    Parameters
    ----------
    input_size : int
        Number of input features per timestep.
    hidden_size : int
        Number of hidden units per LSTM layer. Default 64.
    num_layers : int
        Number of stacked LSTM layers. Default 2.
    dropout : float
        Dropout probability between LSTM layers. Default 0.2.
    output_size : int
        Number of output values (1 for single-step forecast). Default 1.
    """

    def __init__(self,
                 input_size: int,
                 hidden_size: int = 64,
                 num_layers: int = 2,
                 dropout: float = 0.2,
                 output_size: int = 1):
        super(LSTMBaseline, self).__init__()
        # TODO: implement
        pass

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """
        Forward pass.

        Parameters
        ----------
        x : torch.Tensor, shape (batch, seq_len, input_size)
            Input sequence of hourly weather features.

        Returns
        -------
        torch.Tensor, shape (batch, output_size)
            Predicted solar power at the next timestep.
        """
        # TODO: implement
        pass


class GRUBaseline(nn.Module):
    """
    Standard GRU baseline for solar power forecasting.
    Identical architecture to LSTMBaseline but uses GRU cells.

    Parameters
    ----------
    (same as LSTMBaseline)
    """

    def __init__(self,
                 input_size: int,
                 hidden_size: int = 64,
                 num_layers: int = 2,
                 dropout: float = 0.2,
                 output_size: int = 1):
        super(GRUBaseline, self).__init__()
        # TODO: implement
        pass

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """Forward pass — identical structure to LSTMBaseline."""
        # TODO: implement
        pass


class PIMLModel(nn.Module):
    """
    Physics-Informed LSTM model for solar power forecasting.

    Same architecture as LSTMBaseline but trained with the
    custom physics-informed loss function:

        L_total = L_MSE + λ₁·L_max + λ₂·L_night + λ₃·L_monsoon

    The physics constraints are applied externally in the training
    loop via src.physics_loss.piml_loss(). This class defines
    only the neural network architecture.

    Parameters
    ----------
    (same as LSTMBaseline)
    """

    def __init__(self,
                 input_size: int,
                 hidden_size: int = 64,
                 num_layers: int = 2,
                 dropout: float = 0.2,
                 output_size: int = 1):
        super(PIMLModel, self).__init__()
        # TODO: implement — identical to LSTMBaseline architecture
        pass

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """Forward pass — identical to LSTMBaseline."""
        # TODO: implement
        pass
