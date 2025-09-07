`default_nettype none
`timescale 1ns/1ps

module tb ();
  reg  [7:0] ui_in;
  reg  [7:0] uio_in;
  wire [7:0] uo_out;
  wire [7:0] uio_out;
  wire [7:0] uio_oe;
  reg clk, rst_n, ena;

  // Instantiate DUT
  tt_um_adder8 dut (
    .ui_in  (ui_in),
    .uo_out (uo_out),
    .uio_in (uio_in),
    .uio_out(uio_out),
    .uio_oe (uio_oe),
    .ena    (ena),
    .clk    (clk),
    .rst_n  (rst_n)
  );

  // Clock generator
  initial clk = 0;
  always #5 clk = ~clk;

endmodule
