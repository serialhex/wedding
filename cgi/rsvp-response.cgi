#!/usr/bin/env ruby
require "cgi"
require "yaml"

class RsvpResponse
  def initialize
    @cgi = CGI.new("html4")
    @invitees = []
  end

  def load_data
    Dir.glob("rsvp/*.yaml").each do |file|
      @invitees << YAML.load_file(file)
    end
  end

  def render
    @cgi.out() do
      @cgi.html() do
        @cgi.head()
        @cgi.body() do
          res = "YAY!!!<br><br>"
          @invitees.each do |p|
            res << htmlize(p)
            res << "<br><br>"
          end
          res
        end
      end
    end
  end

  def htmlize(yaml)
    out = ''
    out << "Who: " << yaml["first-name"].to_s << ' ' << yaml["last-name"].to_s
    out << "<br>\n"
    out << "Coming? " << yaml["coming"].to_s
    out << "<br>\n"
    out << "Guests: " << yaml["number-guests"].to_s
    out << "<br>\n"
    out << "Address: " << yaml["address"].to_s
    out << "<br>\n"
    out
  end

end

rsvp = RsvpResponse.new
rsvp.load_data
rsvp.render
