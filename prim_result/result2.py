PrimitiveResult(
    [PubResult(
        data=DataBin(
            evs=np.ndarray(<shape=(), dtype=float64>),
            stds=np.ndarray(<shape=(), dtype=float64>),
            ensemble_standard_error=np.ndarray(<shape=(), dtype=float64>)
        ),
        metadata={
            'shots': 10000,
            'target_precision': 0.01,
            'circuit_metadata': {},
            'num_randomizations': 1
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
            'enable_gates': False,
            'enable_measure': False,
            'num_randomizations': 'auto',
            'shots_per_randomization': 'auto',
            'interleave_randomizations': True,
            'strategy': 'active-accum'
        },
        'resilience': {
            'measure_mitigation': False,
            'zne_mitigation': False,
            'pec_mitigation': False
        },
        'version': 2
    }
)