PrimitiveResult(
    [PubResult(
        data=DataBin(
            evs=np.ndarray(<shape=(), dtype=float64>),
            stds=np.ndarray(<shape=(), dtype=float64>),
            evs_noise_factors=np.ndarray(<shape=(3,), dtype=float64>),
            stds_noise_factors=np.ndarray(<shape=(3,), dtype=float64>),
            ensemble_stds_noise_factors=np.ndarray(<shape=(3,), dtype=float64>),
            evs_extrapolated=np.ndarray(<shape=(2, 4), dtype=float64>),
            stds_extrapolated=np.ndarray(<shape=(2, 4), dtype=float64>)
        ),
        metadata={
            'shots': 10016,
            'target_precision': 0.01,
            'circuit_metadata': {},
            'resilience': {'zne': {'extrapolator': 'exponential'}},
            'num_randomizations': 32
        }
    )],
    metadata={
        'dynamical_decoupling': {
            'enable': True,
            'sequence_type': 'XpXm',
            'extra_slack_distribution': 'middle',
            'scheduling_method': 'alap'
        },
        'twirling': {
            'enable_gates': True,
            'enable_measure': True,
            'num_randomizations': 'auto',
            'shots_per_randomization': 'auto',
            'interleave_randomizations': True,
            'strategy': 'active-accum'
        },
        'resilience': {
            'measure_mitigation': True,
            'zne_mitigation': True,
            'pec_mitigation': False,
            'zne': {
                'noise_factors': [1.0, 3.0, 5.0],
                'extrapolator': ['exponential', 'linear'],
                'extrapolated_noise_factors': [0, 1.0, 3.0, 5.0]
            }
        },
        'version': 2
    }
)