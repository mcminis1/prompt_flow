import pytest
from prompt_flow.graph import Graph, SuperList
from functions import sub_1, add_1, mult_2



@pytest.mark.asyncio
async def test_fan_out():
    # fan out example
    g = Graph()
    g.add_nodes([sub_1, add_1, mult_2])

    i_0 = g.input(name="n")
    o_1 = g.add_1(i_0)
    g.outputs = g.mult_2(o_1) # q
    g.outputs += g.sub_1(o_1) # p
    assert len(g.outputs) == 2

    v = await g(n=1)
    print(v)
    assert len(v) == 2
    # TODO(jeremy): need a better way to manage multiple outputs
    assert v[0].q == 4
    assert v[1].p == 1
    