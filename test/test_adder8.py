import cocotb
from cocotb.triggers import Timer


@cocotb.test()
async def test_simple_addition(dut):
    """Test a few simple additions"""

    # Reset and enable
    dut.rst_n.value = 1
    dut.ena.value = 1

    # Case 1: 12 + 7 = 19
    dut.ui_in.value = 12
    dut.uio_in.value = 7
    await Timer(10, units="ns")
    assert dut.uo_out.value == 19, f"Expected 19, got {int(dut.uo_out.value)}"

    # Case 2: 240 + 15 = 255
    dut.ui_in.value = 240
    dut.uio_in.value = 15
    await Timer(10, units="ns")
    assert dut.uo_out.value == 255, f"Expected 255, got {int(dut.uo_out.value)}"

    # Case 3: 170 + 85 = 255
    dut.ui_in.value = 170
    dut.uio_in.value = 85
    await Timer(10, units="ns")
    assert dut.uo_out.value == 255, f"Expected 255, got {int(dut.uo_out.value)}"

    # Case 4: 255 + 1 = 0 (wrap-around, carry ignored)
    dut.ui_in.value = 255
    dut.uio_in.value = 1
    await Timer(10, units="ns")
    assert dut.uo_out.value == 0, f"Expected 0, got {int(dut.uo_out.value)}"
