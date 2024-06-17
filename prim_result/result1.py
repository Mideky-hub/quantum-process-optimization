#Result 1: 
PrimitiveResult(
    [
        PubResult(
            data=DataBin(
                evs=np.ndarray(shape=(), dtype=float64),
                stds=np.ndarray(shape=(), dtype=float64),
                ensemble_standard_error=np.ndarray(shape=(), dtype=float64)
            ),
            metadata={
                'shots': 10016,
                'target_precision': 0.01,
                'circuit_metadata': {},
                'resilience': {},
                'num_randomizations': 32
            }
        )
    ],
    metadata={
        'dynamical_decoupling': {
            'enable': True,
            'sequence_type': 'XpXm',
            'extra_slack_distribution': 'middle',
            'scheduling_method': 'alap'
        },
        'twirling': {
            'enable_gates': False,
            'enable_measure': True,
            'num_randomizations': 'auto',
            'shots_per_randomization': 'auto',
            'interleave_randomizations': True,
            'strategy': 'active-accum'
        },
        'resilience': {
            'measure_mitigation': True,
            'zne_mitigation': False,
            'pec_mitigation': False
        },
        'version': 2
    }
)