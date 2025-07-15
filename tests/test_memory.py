import pytest

from memory import utils
from memory.long_term_memory import LongTermMemory
from memory.short_term_memory import ShortTermMemory


def test_short_term_memory():
    stm = ShortTermMemory(memory_limit=3)

    stm.add_memory({1: "thanks"})
    stm.add_memory({2: "for"})
    stm.add_memory({3: "all"})
    stm.add_memory({4: "the"})
    stm.add_memory({5: "fish"})

    assert len(stm.get_memories()) == 3
    assert stm.get_memories() == [{5: "fish"}, {4: "the"}, {3: "all"}]


def test_long_term_memory():
    stm = ShortTermMemory(memory_limit=3)
    ltm = LongTermMemory()

    stm.add_memory({"Hello": "world!"})
    stm.add_memory({"Math": "2 + 2 = 4"})

    ltm.add_short_term_memories(stm)

    key = list(ltm.get_memory().keys())[0]
    ltm_memory = ltm.get_memory()

    assert ltm_memory[key] == [{"Math": "2 + 2 = 4"}, {"Hello": "world!"}]


@pytest.mark.integration
def test_summarise_memory_option():
    stm = ShortTermMemory()
    ltm = LongTermMemory()

    stm.add_memory({"User_01": "Complained that their Xbox arrived late"})
    stm.add_memory({"User_02": "Thankful that the playstation did not arrive broken"})
    stm.add_memory({"User_03": "Bought four new games at Christmas"})
    stm.add_memory({"User_02": "Needs a new controller to play with their neighbour"})

    ltm.add_short_term_memories(stm)

    memory = ltm.get_summary()

    judgement = utils.send_message(
        user_prompt=f"""
    Does this summary reflect the data acccurately? Return only TRUE if true, else FALSE.

    SUMMARY: {memory}
    
    DATA: {stm.get_memories()}
    """
    )

    assert judgement == "TRUE"
