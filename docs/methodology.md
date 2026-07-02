# QX-01 Methodology Notes

## Data Pipeline

### NASA POWER Variables
- **GHI** (ALLSKY_SFC_SW_DWN): Global Horizontal Irradiance [W/m²]
- **CLRSKY** (CLRSKY_SFC_SW_DWN): Clear-sky GHI [W/m²]
- **T2M**: 2-metre air temperature [°C]
- **RH2M**: 2-metre relative humidity [%]
- **PRECIP** (PRECTOTCORR): Corrected precipitation [mm/hour]
- **WS10M**: 10-metre wind speed [m/s]

### Feature Engineering
| Feature | Formula | Purpose |
|---------|---------|---------|
| K_T | GHI / CLRSKY, clipped [0,1] | Clearness index |
| θ_z | PVLib solarposition | Solar zenith angle |
| season | Month-based label | Seasonal stratification |
| rolling_precip_24h | PRECIP.rolling(24).sum() | Extended rainfall signal |
| irradiance_drop_rate | GHI[t] - GHI[t-1] | Cloud transition speed |
| extreme_precip_flag | PRECIP > 95th percentile | Extreme event indicator |
| extreme_ghi_flag | GHI < 10th percentile | Low-irradiance indicator |
| P_max | GHI × η × A × (1 - γ(T_cell - T_ref)) | Physical upper bound |

### PVLib Parameters
- Panel efficiency η = 0.20 (20%)
- Panel area A = 5 m²
- Temperature coefficient γ = -0.004 /°C
- Reference temperature T_ref = 25°C
- Tilt = 23° (latitude-optimised for Sylhet)
