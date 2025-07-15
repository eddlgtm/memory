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
