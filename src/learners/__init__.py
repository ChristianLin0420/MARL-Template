from .dmaq_qatten_learner import DMAQ_qattenLearner
from .q_learner import QLearner
from .nq_learner import NQLearner
from .coma_learner import COMALearner
from .qtran_learner import QLearner as QTranLearner
from .ppo_learner import PPOLearner
from .nq_learner_data_augmentation import NQLearnerDataAugmentation

REGISTRY = {}

REGISTRY["q_learner"] = QLearner
REGISTRY["nq_learner"] = NQLearner
REGISTRY["coma_learner"] = COMALearner
REGISTRY["qtran_learner"] = QTranLearner
REGISTRY["ppo_learner"] = PPOLearner
REGISTRY["dmaq_qatten_learner"] = DMAQ_qattenLearner
REGISTRY["q_learner_data_augmentation"] = NQLearnerDataAugmentation
