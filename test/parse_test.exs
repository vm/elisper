defmodule ParseTest do
  require Parse
  use ExUnit.Case, async: true
  doctest Parse

  test "parse variable valid" do
    assert Parse.parse("+") == {:variable, :add}
  end

  test "parse string containing integer" do
    assert Parse.parse(~s("42")) == {:string, "42"}
  end
end
