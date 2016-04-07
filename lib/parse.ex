defmodule Parse do
  @moduledoc """
  This is the parsing module for Elisper
  """

  @doc """
  Attempts to parse `text` into the Elisper's internal representation.

  ## Examples

    iex> Parse.parse("(+ 1 1)")
    [:add, 1, 1]
    iex> Parse.parse("(+ \"what\" (+ \"is\" \"up\"))")
    [:add "what" [:add "is" "up"]]
    iex> Parse.parse("(+ 1 1))")
    :error
    iex> Parse.parse("+ 1 1")
    :error

  Returns `:error` if unsucessful.
  """
  def parse(text) do
    parse_variable(text) || parse_string(text) || parse_integer(text) || parse_list(text) || :error
  end

  defp parse_variable(text) do
    case text do
      "+" -> :add
      _ -> nil
    end
  end

  defp parse_string(text) do
    quote_char = ~s(")
    cond do
      String.first(text) == quote_char and String.last(text) == quote_char ->
        String.slice(text, 1..-2)
      true -> nil
    end
  end

  defp parse_integer(text) do
    case Integer.parse text do
      {int, ""} -> int
      _ -> nil
    end
  end

  defp parse_list(text) do
    char_stream = Stream.unfold(text, &String.next_codepoint/1)

    handle_char = fn
      "(", {"" = empty, 0, []} -> {empty, 1, []}
      "(" = opening, {temp, 1, sexps} -> {temp <> opening, 2, sexps}
      ")", {temp, 1, sexps} -> {"", 0, sexps ++ [parse temp]}
      " ", {temp, 1, sexps} -> {"", 1, sexps ++ [parse temp]}
      ")" = closing, {temp, depth, sexps} -> {temp <> closing, depth - 1, sexps}
      char, {temp, depth, sexps} -> {temp <> char, depth, sexps}
    end

    case Enum.reduce char_stream, {"", 0, []}, handle_char do
      {"", 0, sexps} -> sexps
      _ -> nil
    end
  end
end
