defmodule ParseTest do
  require Parse
  use ExUnit.Case, async: true

  test "parse variable valid" do
    assert Parse.parse("+") == :add
  end

  test "parse string" do
    assert Parse.parse(~s("hello")) == "hello"
  end

  test "parse string containing integer" do
    assert Parse.parse(~s("42")) == "42"
  end

  test "parse integer valid" do
    assert Parse.parse("42") == 42
  end

  test "parse list add" do
    assert Parse.parse("(+ 1 1)") == [:add, 1, 1]
  end
end
